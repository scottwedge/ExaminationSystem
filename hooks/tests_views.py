import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.management import call_command
from unittest.mock import patch

def testgitlab(self):
    
    event = self.META.get('HTTP_X_GITLAB_EVENT', 'ping')
    self.assertTrue(event.status_code, 200)
    #self.assertFalse(event.status_code, 300)
    #self.assertFalse(event.http.HTTP_X_GITLAB_EVENT, 'ping')
    
