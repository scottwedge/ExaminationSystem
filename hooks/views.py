#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

#Create your views here.

#@require_POST
@csrf_exempt
def gitlab(request):
    #Process Event...
    event = request.META.get('HTTP_X_GITLAB_EVENT', 'ping')

    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        # Do something...
        #HERE IS WHERE WE CALL THE pull/migrate commands
        return HttpResponse('success')

    # In case we receive an event that's not ping or push
    return HttpResponse(status=204)