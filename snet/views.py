__author__ = 'Paul'

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from implementationManager.views import returnUserProjects


def jSerializeData(inputData):
    jsonSerializer = serializers.get_serializer('json')
    json_serializer = jsonSerializer()
    json_serializer.serialize(inputData)
    outputData = json_serializer.getvalue()
    return (outputData)


def logTheUserOut(request):
    if (request.method == 'GET'):
        logout(request)
        endSession = True
        return render_to_response('registration/auth.html', {'endSession': endSession},
                                  context_instance=RequestContext(request))
    else:
        raise Http404


def returnRootLanding(request):
    if (request.method == 'GET'):
        p = returnUserProjects(request.user.id)
        u = request.user
        return render_to_response('djangoLanding.html', {'u': u, 'p': p},
                                  context_instance=RequestContext(request))
    else:
        raise Http404


def returnUserObject(request):
    if (request.method == 'GET'):
        u = [False]
        if (request.user.is_authenticated()):
            u = jSerializeData(User.objects.filter(id=request.user.id))
        return HttpResponse(u)
    else:
        raise Http404