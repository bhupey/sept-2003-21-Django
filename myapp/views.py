from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request: HttpResponse):
    return HttpResponse("<h1> Hello I'm Learning python.")

def ahome(request):
    return HttpResponse("<h1>This is Root directory</h2>")

def root(request):
    return render(request, template_name="myapp/root.html")
