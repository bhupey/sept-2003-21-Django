from django.shortcuts import render
from .models import Student, StudentProfile

# Create your views here.
def student(request):
    student= [
        {"name":"jon", "age":30, "address":"KTM"},
        {"name":"jane", "age":20, "address":"PKR"},
        {"name":"srijan", "age":20, "address":"Buddhanagar"},
        {"name":"Anukul", "age":60, "address":"Kadaghari"},
    ]
    return render(request, template_name="temp_inheritance/student.html", context={"name":student})

def model_student(request):
    student = Student.objects.all()
    return render(request, template_name="temp_inheritance/model_student.html", context={"students":student})


def profile(request):
    st = StudentProfile.objects.all()
    return render(request, template_name="temp_inheritance/profile.html", context={"students":st})