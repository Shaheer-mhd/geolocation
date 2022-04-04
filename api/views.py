from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests


@api_view(['GET', 'POST'])
def get_api(request):
    if request.method == 'GET':
        return JsonResponse("api project", safe=False)
    else:
        data = request.data
        address = data.get('address')
        return JsonResponse(address)
