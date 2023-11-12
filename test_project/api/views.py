from api import constants, service
from rest_framework import decorators as rf_decorators
from rest_framework import views, viewsets

from metaclass import decorators


@decorators.metaclass(decorated=True)
@rf_decorators.api_view(constants.http_method_names)
def echo_view(request):
    return service.echo(request)


class EchoAPIView(views.APIView):
    @decorators.metaclass(decorated=True)
    def get(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def post(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def put(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def patch(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def delete(self, request):
        return service.echo(request)


class EchoViewSet(viewsets.GenericViewSet):
    @decorators.metaclass(decorated=True)
    def list(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def retrieve(self, request, *_, **__):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def create(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def destroy(self, request, *_, **__):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def update(self, request, *_, **__):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    def partial_update(self, request, *_, **__):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    @rf_decorators.action(methods=constants.http_method_names, detail=False)
    def echo(self, request):
        return service.echo(request)

    @decorators.metaclass(decorated=True)
    @rf_decorators.action(methods=constants.http_method_names, detail=True)
    def detail_echo(self, request, *_, **__):
        return service.echo(request)
