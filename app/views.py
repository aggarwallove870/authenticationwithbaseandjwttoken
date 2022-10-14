from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from app.serializer import UserSerializers
from django.http import HttpResponse,HttpResponseGone,response
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

@csrf_exempt
@api_view(['GET', 'POST'])
#@authentication_classes([BasicAuthentication])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def save_username(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        print(serializer,"==========================")
        if serializer.is_valid():
          serializer.save()
          
          
          serializer= UserSerializers(User.objects.all(),many=True)

        return Response(serializer.data)
    if request.method == 'GET':
      user = User.objects.all()
      serializer= UserSerializers(user,many=True)
      print(type(serializer))

    return Response(serializer.data)
   
@api_view(['DELETE'])
def eventdelete(request,pk):
  event= User.objects.get(id=pk)
  event.delete()
  return Response("Delete")

@api_view(['PATCH'])
def eventupdate(request,pk):
  event=User.objects.get(id=pk)
  serializer=UserSerializers(instance=event,data=request.data)
  if serializer.is_valid():
      serializer.save()
  return Response("Update Succesfully")