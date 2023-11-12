import logging
from unittest import mock

from api import constants
from django import test, urls
from rest_framework import status


class EchoTestCase(test.TestCase):  # pylint: disable=R0902
    def setUp(self):
        super().setUp()

        logging.disable(logging.CRITICAL)

        self.kwargs = {"pk": 1}
        self.data = {"message": "Hello, world!"}
        self.content_type = "application/json"

        self.function_url = urls.reverse("function")
        self.class_url = urls.reverse("class")
        self.viewset_list_url = urls.reverse("viewset-list")
        self.viewset_detail_url = urls.reverse("viewset-detail", kwargs=self.kwargs)
        self.viewset_echo = urls.reverse("viewset-echo")
        self.viewset_detail_echo = urls.reverse(
            "viewset-detail-echo", kwargs=self.kwargs
        )

    def single(self, client_function, url):
        with mock.patch(
            "metaclass.middleware.MetaclassMiddleware.metaclass_found",
        ) as mock_metaclass_found:
            response = client_function(
                url, data=self.data, content_type=self.content_type
            )
            self.assertTrue(mock_metaclass_found.called)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            response_json = response.json()
            self.assertEqual(response_json, self.data)

    def plain(self, test_name, url):
        logging.debug(test_name)
        for method in constants.http_method_names:
            logging.debug("Method: %s", method)
            client_function = getattr(self.client, method)
            self.single(client_function, url)

    def test_function(self):
        self.plain("function", self.function_url)

    def test_class(self):
        self.plain("class", self.class_url)

    def test_viewset(self):
        logging.debug("viewset")

        self.single(self.client.get, self.viewset_list_url)
        self.single(self.client.post, self.viewset_list_url)

        self.single(self.client.get, self.viewset_detail_url)
        self.single(self.client.put, self.viewset_detail_url)
        self.single(self.client.patch, self.viewset_detail_url)
        self.single(self.client.delete, self.viewset_detail_url)

        self.plain("viewset action", self.viewset_echo)
        self.plain("viewset detail action", self.viewset_detail_echo)
