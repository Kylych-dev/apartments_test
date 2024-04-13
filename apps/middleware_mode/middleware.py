import logging
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class MainModelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info('Request received')

        if settings.MAINTENANCE_MODE:
            logger.warning('Application is in maintenance mode!')
            return HttpResponse('Applicaiton is in maintenance mode. Please try again later.')

        response = self.get_response(request)

        return response
    



    '''
    
class MainModelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    '''