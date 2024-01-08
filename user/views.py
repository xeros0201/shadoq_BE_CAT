
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#GET - POST - PUT - DELETE
# trycatch

@api_view(['GET'])
def GET(request):
   return Response( data="{ message:'success'}",  status=status.HTTP_200_OK)

@api_view(['POST'])
def POST(request):
   return Response( data="{ message:'success'}",  status=status.HTTP_200_OK)