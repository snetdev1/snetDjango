from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from models import *


def jSerializeData(inputData):
    jsonSerializer = serializers.get_serializer('json')
    json_serializer = jsonSerializer()
    json_serializer.serialize(inputData)
    outputData = json_serializer.getvalue()
    return (outputData)


@login_required
def displayMetaData(request):
    if (request.method == 'GET'):


        metaValues = request.META.items()
        u = request.user

        return render_to_response('metadata.html', {'u': u, 'metaData': metaValues},
                                  context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def returnMetaDataAsJSON(request):
    if (request.method == 'GET'):
        data = jSerializeData(request.META.items())
        return HttpResponse(data)
    else:
        raise Http404


def returnUserProjects(userID):
    userProjects = projectUser.objects.filter(user=userID, project__active=True).values('project')
    projects = project.objects.filter(id__in=userProjects)

    return projects
