from django.shortcuts import render
from django.views.generic import ListView
from .models import Jobs
# Create your views here.

class JobsList(ListView):
    model = Jobs


def jobdetiel(request,id):
    job = Jobs.objects.get(id=id)
    return render(request , 'single.html', {'job':job})