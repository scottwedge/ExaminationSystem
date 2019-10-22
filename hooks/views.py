#from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.management import call_command
#Create your views here.

#instantiate logger
logger = logging.getLogger(__name__)

#@require_POST
@csrf_exempt
def gitlab(request):
    #Process Event...
    event = request.META.get('HTTP_X_GITLAB_EVENT', 'ping')
    logger.info('notification of successful build received')


   # if event == 'ping':
   #     return HttpResponse('pongify')
   # elif event == 'pull':
        # Do something...
        #HERE IS WHERE WE CALL THE pull/migrate commands
    call_command('makemigrations')
    call_command('migrate')
    return HttpResponse('success')

    # In case we receive an event that's not ping or push
    #return HttpResponse(status=204)