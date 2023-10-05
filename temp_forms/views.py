from django.shortcuts import render, redirect
from temp_inheritance.models import Student

# Create your views here.
def student_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        Student.objects.create(name=name, email=email, age=age)
        return redirect("student")
    # print(request.method)
    # print(request.POST)
    return render(request, template_name="temp_forms/student_form.html")