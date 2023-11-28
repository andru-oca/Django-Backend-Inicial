from django.utils.deprecation import MiddlewareMixin


class CorsMiddlewareMixin(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, DELETE"
        response["Access-Control-Allow-Headers"] = "*"
        return response
