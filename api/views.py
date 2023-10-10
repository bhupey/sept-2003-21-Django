from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student

# Create your views here.

def hello_world(request):
    response = {"message": "Hello World"}
    return JsonResponse(response)


class MessageView(APIView):
    def get(self, *args, **kwargs):
        return Response([
            {"name":"harry", "address":"KTM", "age":20},
            {"name":"anukul", "address":"PKR", "age":20},
            {"name":"srijan", "address":"NPJ", "age":20},
              
        ])
    

class SimpleStudentView(APIView):
    def get(self, *args, **kwarks):
        student = Student.objects.get(id=kwarks['id'])
        return Response({
            "name":student.name,
            "email":student.email,
            "age":student.age,
            "classroom":student.classroom.name
        })
    
class SimpleStudentListView(APIView):
    def get(self, *args, **kwarks):

        queryset= Student.objects.all()
        response =[]
        for student in queryset:
            response.append({
                "name":student.name,
                "email":student.email,
                "age":student.age,
                "classroom":student.classroom.name
            })
        return Response(response)







    
# class StudentListView(ListView):
#     queryset = Student.objects.all()
#     template_name= "classbased/student.html"
#     context_object_name="students"