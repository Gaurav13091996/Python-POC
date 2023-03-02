from django.shortcuts import render
from django.shortcuts import render
from .models import Employee_Details
from rest_framework.views import APIView
from rest_framework.viewsets import views
from .serializer import Employeeserializer
from rest_framework.response import Response
# Create your views here.

def show(r):
    results=Employee_Details.objects.all()
    print(results)
    return render(r,'display.html',{'data':results})

class Employee_list(APIView):
    def get(self,request):
        Employees = Employee_Details.objects.all()
        employee_serializer = Employeeserializer(Employees, many=True)
        return Response(employee_serializer.data)
