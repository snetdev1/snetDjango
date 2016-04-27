__author__ = 'Paul'

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from implementationManager.views import returnUserProjects
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from social.apps.django_app.views import _do_login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from social.apps.django_app.utils import load_strategy, load_backend
from rest_framework import status
from social.apps.django_app.utils import psa, strategy


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




@csrf_exempt
@strategy()
def auth_by_token(request, backend):
    uri = ''
    strategy = load_strategy(request)
    backend = load_backend(strategy, backend, uri)
    user = request.user
    user = backend.do_auth(
        access_token=request.data.get('access_token'),
        user=user.is_authenticated() and user or None
    )
    if user and user.is_active:
        return user# Return anything that makes sense here
    else:
        return None


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def social_register(request):
    auth_token = request.data.get('access_token', None)
    backend = request.data.get('backend', None)
    if auth_token and backend:
        try:
            user = auth_by_token(request, backend)
        except Exception, err:
            return Response(str(err), status=400)
        if user:
            uri = ''
            strategy = load_strategy(request)
            backend = load_backend(strategy, backend, uri)
            _do_login(backend , user, strategy)

            return Response( "User logged in", status=status.HTTP_200_OK )
        else:
            return Response("Bad Credentials", status=403)
    else:
        return Response("Bad request", status=400)

@login_required
def displayMetaData(request):
    if (request.method == 'GET'):


        metaValues = request.META.items()
        u = request.user

        return render_to_response('metadata.html', {'u': u, 'metaData': metaValues},
                                  context_instance=RequestContext(request))
    else:
        raise Http404