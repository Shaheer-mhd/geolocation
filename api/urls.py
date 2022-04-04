from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('POST/getAddressDetails/', views.get_api, name='get_api'),

]
