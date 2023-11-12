import logging


class MetaclassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def get_meta(self, view):
        return getattr(view, "Meta", None)

    def get_metaclass(self, request, view_func):
        metaclass = self.get_meta(view_func)
        if metaclass is not None:
            # function
            return metaclass

        cls = getattr(view_func, "cls", None)
        if cls is None:
            return None

        method = request.method.lower()
        actions = getattr(view_func, "actions", None)

        if actions is None:
            view = getattr(cls, method)
            metaclass = self.get_meta(view)
            # class
            return metaclass

        try:
            action = actions[method]
        except KeyError:
            return None
        view = getattr(cls, action, None)
        if view is None:
            return None
        metaclass = self.get_meta(view)
        # viewset
        return metaclass

    def metaclass_not_found(self):
        logging.debug("metaclass is None.")

    def metaclass_found(self):
        logging.debug("metaclass is set.")

    def process_view(self, request, view_func, _, __):
        logging.debug("process_view")
        metaclass = self.get_metaclass(request, view_func)
        if metaclass is None:
            self.metaclass_not_found()
        else:
            self.metaclass_found()
        setattr(request, "metaclass", metaclass)
