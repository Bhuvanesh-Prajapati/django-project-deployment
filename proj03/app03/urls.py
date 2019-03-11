from django.urls import path
from app03 import views

app_name = 'app03'

# TEMPLATE TAGGING
urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
