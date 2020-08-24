from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import (
  ListAPIView, 
  RetrieveAPIView,
  UpdateAPIView,
  RetrieveUpdateAPIView,
  ListCreateAPIView
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models, serializers


# Create your views here.
def index(request):
    return HttpResponse('Hello')

class MemberDetailView(RetrieveUpdateAPIView):
  queryset = models.Mem.objects.all()
  serializer_class = serializers.MemberSerializer 

@api_view()
def userApi(request):
    users = models.Mem.objects.all()
    response = serializers.MemberSerializer(users, many = True)
    return Response(response.data)
