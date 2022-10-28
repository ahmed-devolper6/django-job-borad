from django.urls import path
from .views import JobsList , jobdetiel
app_name = 'jobs'

urlpatterns = [
    path('',JobsList.as_view(),name='job_list'),
    path('<int:id>',jobdetiel,name='job_detil')
]