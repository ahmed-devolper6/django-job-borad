from django.shortcuts import render , redirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Jobs
from .forms import ApplyForm , JobForm
# Create your views here.

class JobsList(ListView):
    model = Jobs


def jobdetiel(request,id):
    job = Jobs.objects.get(id=id)
    #apply
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = ApplyForm()
    return render(request , 'single.html', {'job':job,'form1':form})


@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})