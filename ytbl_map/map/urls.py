from django.urls import path
import map.views

app_name = 'ytbl'

urlpatterns = [
    path('', map.views.showMap, name='showMap'),
]