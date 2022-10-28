from django.shortcuts import render

# Create your views here.
def contant(request):
    return render(request ,'contant.html',{})