from django.shortcuts import render
from rest_framework import viewsets
from myProject.models import Employee
from myProject.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializer