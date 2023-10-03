from django.shortcuts import render

# Create your views here.
def static_home(request):
    return render(request, template_name="static_render/static_home.html", context={"title":"Staic Test"})

def index(request):
    return render(request, template_name="static_render/index.html")