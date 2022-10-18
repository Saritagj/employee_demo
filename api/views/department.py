from django.http import HttpResponse, HttpRequest
from api.utils.status_code import *
from api.utils.constant import *
from rest_framework.views import APIView
from api.models import MDepartment
from rest_framework.response import Response
from api.serializers.department import DepartmentSerializer


class Department(APIView):
    def post(self, request: HttpRequest) -> HttpResponse:
        """To insert the department data

        Args:
            request : Post Request object

        Returns:
            Response : json data of Department
        """
        try:
            data = request.data
            serializer = DepartmentSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create Department in the DB
            serializer.save()

            # Return Response to User
            response = Response(serializer.data)
            return response

        except Exception as exception:
            response = HttpResponse(
                UNEXPECTED_EXCEPTION % exception, status=Status.STATUS_CODE_400
            )
            return response

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        """To fetch the data of all department or to fetch data of particular department id

        Args:
            request : Get request object

        Returns:
            Response : Json data of all department or for particular department id
        """
        try:
            if pk:

                data = MDepartment.objects.get(id=pk)
                serializer = DepartmentSerializer(data)

            else:

                data = MDepartment.objects.all()
                serializer = DepartmentSerializer(data, many=True)

            return Response(serializer.data)

        except Exception as exception:
            response = HttpResponse(
                DEPARTMENT_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response

    def put(self, request: HttpRequest, pk: int) -> HttpResponse:
        """To updated the department data for particular id

        Args:
            request : Put request object
            pk : id of department . Defaults to None.

        Returns:
            Response : Updated data of department for department id
        """

        try:
            update = MDepartment.objects.get(pk=pk)
            serializer = DepartmentSerializer(
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

        except Exception as exception:
            response = HttpResponse(
                DEPARTMENT_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        """To delete department data for particular department id or all data of department

        Args:
            pk : id of department. Defaults to None.

        Returns:
            Response: message
        """
        try:
            if pk:
                delete = MDepartment.objects.get(pk=pk)
                delete.delete()

            else:
                delete = MDepartment.objects.all()
                delete.data()

            return Response({"message": "Data  Deleted Successfully"})

        except Exception as exception:
            response = HttpResponse(
                DEPARTMENT_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response
