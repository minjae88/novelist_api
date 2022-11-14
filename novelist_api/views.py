from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import requests as res

@api_view(['POST'])
def TextApi(request):
    url = "http://www.naver.com"
    response = res.post(url, data=request.data)
    return Response(response.text)
