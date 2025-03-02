from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.headers.get('Authentication')
        if auth_header != settings.AUTHENTICATION_TOKEN:
            return JsonResponse({'error': 'Invalid authentication header'}, status=401)
