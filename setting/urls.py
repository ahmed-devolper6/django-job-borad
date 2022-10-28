from django.urls import path, re_path
from .views import contant

app_name = 'setting'

urlpatterns = [
    path('',contant,name='about')
]