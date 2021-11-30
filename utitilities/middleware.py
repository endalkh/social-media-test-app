from . import utils
from rest_framework.authtoken.models import Token
from re import sub


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        utils.remove_current_user()
        return response

    def process_request(self, request):
        header_token = request.META.get("HTTP_AUTHORIZATION", None)
        if header_token is not None:
            token = sub("Token ", "", header_token)
            try:
                token_obj = Token.objects.get(key=token)
                request.user = token_obj.user
                utils.set_current_user(request.user)
            except Token.DoesNotExist:
                pass
        return None
