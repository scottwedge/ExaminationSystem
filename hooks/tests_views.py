#from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.management import call_command
#Create your views here.

#@require_POST
@csrf_exempt
def testgitlab(self):
    #Process Event...
    event = self.META.get('HTTP_X_GITLAB_EVENT', 'ping')
    
  
    call_command('makemigrations')
    call_command('migrate')
    self.assertTrue(event, True)

    # In case we receive an event that's not ping or push
    #return HttpResponse(status=204)