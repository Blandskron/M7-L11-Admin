from django.utils.deprecation import MiddlewareMixin

class CustomSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.session.get('visits'):
            request.session['visits'] = 0
        request.session['visits'] += 1
