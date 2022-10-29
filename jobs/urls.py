from django.urls import path
from .views import JobsList , jobdetiel , add_job
app_name = 'jobs'

urlpatterns = [
    path('',JobsList.as_view(),name='job_list'),
    path('<int:id>',jobdetiel,name='job_detil'),
    path('add_jobs',add_job,name='add_job')
]