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
        output = data.get('output_format')
        formatting = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'
        r = requests.get(formatting)
        return JsonResponse(r, safe=False)


