from django.shortcuts import render
from .models import Employee_Details
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import Employeeserializer
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


# Create your views here.
def show(r):
    results=Employee_Details.objects.all()
    print(results)
    return render(r,'show.html',{'data':results})



class Employee_list(viewsets.ModelViewSet):
    queryset =Employee_Details.objects.all()
    serializer_class = Employeeserializer

class Employee_jwtauth(viewsets.ModelViewSet):
    queryset =Employee_Details.objects.all()
    serializer_class = Employeeserializer

    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]


class Employee_Basicauth(viewsets.ModelViewSet):
    queryset =Employee_Details.objects.all()
    serializer_class = Employeeserializer

    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]




