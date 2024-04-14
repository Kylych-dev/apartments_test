import logging
from django.test import TestCase, Client, override_settings


class MainModelMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()
        logging.disable(logging.CRITICAL)

    @override_settings(MAINTENANCE_MODE=True)
    def test_response_when_mode_on(self):
        response = self.client.get('/')
        self.assertContains(
            response,
            '*-*-**--*-*-*-*'
            )
        
    
    @override_settings(MAINTENANCE_MODE=False)
    def test_response_when_mode_off(self):
        response = self.client.get('/')

        self.assertContains(
            response,
            'We are in!'
            )
        self.assertTemplateUsed(response, 'index.html')