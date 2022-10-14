from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee, Company, Department
from rest_framework.response import Response
from .serializers import (
    EmployeeSerializer,
    CompanySerializer,
    DepartmentSerializer,
)
from rest_framework.response import Response


class EmployeeAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = EmployeeSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Employee in the DB
        serializer.save()

        # Return Response to User

        response = Response(serializer.data)

        return response

    def get(self, request, pk=None):
        
        if pk:
            # print("first")
            data = Employee.objects.get(pk=pk)
            # print(data.company.name)
            # cmp = Company.objects.get(pk=data.company.id)
            # print(cmp)
            serializer = EmployeeSerializer(data)

        else:
           
            data = Employee.objects.all()
            serializer = EmployeeSerializer(data, many=True)

        return Response(serializer.data)

    def put(self, request, pk=None):
        update = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(
            instance=update, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            "message": "Data Updated Successfully",
            "data": serializer.data,
        }

        return response

    def delete(self, request, pk):
        delete = Employee.objects.get(pk=pk)

        delete.delete()

        return Response({"message": "Data  Deleted Successfully"})


class CompanyAPIView(APIView):
    
    def post(self, request, format=None):
        data = request.data
        serializer = CompanySerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Company in the DB
        serializer.save()

        # Return Response to User
        response = Response(serializer.data)

        return response
    
    def put(self, request, pk=None):
        update = Company.objects.get(pk=pk)
        serializer = CompanySerializer(
            instance=update, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            "message": "Data Updated Successfully",
            "data": serializer.data,
        }

        return response


class DepartmentAPIView(APIView):
    
    def post(self, request, format=None):
        data = request.data
        serializer = DepartmentSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Department in the DB
        serializer.save()

        # Return Response to User
        response = Response(serializer.data)

        return response
