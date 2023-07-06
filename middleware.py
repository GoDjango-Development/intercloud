from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .urls import urlpatterns
from django.urls import resolve, get_resolver
from django.utils.deprecation import MiddlewareMixin 

class IntercloudMiddleware(MiddlewareMixin):
    #response_redirect_class = HttpResponsePermanentRedirect

    #def process_request(self, request: HttpRequest):
    #    pass

    def process_response(self, request: HttpRequest, response: HttpResponse):
        resolved = resolve(request.path)
        if response.status_code == 200 and len(resolved.tried) > 0 and  len(resolved.tried[-1]) > 1 and resolved.tried[-1][1] in urlpatterns:
            if not response.streaming and not response.has_header("Access-Control-Allow-Origin"):
                origin = request.headers.get("Origin", None)
                if origin is None:
                    origin = request.headers.get("Referer", None)
                if origin is not None:
                    response.headers["Access-Control-Allow-Origin"] = origin
        return response
