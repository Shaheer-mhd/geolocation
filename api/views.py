from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from dicttoxml import dicttoxml


@api_view(['GET', 'POST'])
def get_api(request):
    if request.method == 'GET':
        return JsonResponse("api project", safe=False)
    else:
        data = request.data
        address = data.get('address')
        output = data.get('output_format')
        formatting = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSy' \
                     f'COD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'
        response = requests.get(url=formatting)
        response = response.json()
        coordinates = response['results'][0]['geometry']['location']
        data = {}
        data.update({"coordinates": coordinates})
        data.update({"address": address})
        if output == 'json':
            return JsonResponse(data, safe=False)
        else:
            xml_data = dicttoxml(data, attr_type=False)
            return Response(xml_data, status=201)
