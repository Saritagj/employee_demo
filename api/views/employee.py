from django.http import HttpResponse, HttpRequest
from api.utils.status_code import *
from api.utils.constant import *
from rest_framework.views import APIView
from api.models import TEmployee
from rest_framework.response import Response
from api.serializers.employee import EmployeeSerializer


class Employee(APIView):
    def post(self, request: HttpRequest) -> HttpResponse:
        """To insert the employee data

        Args:
            request : Post request object

        Returns:
            Response: Json of employee data
        """
        try:
            data = request.data
            serializer = EmployeeSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create Employee in the DB
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
        """To fetch the data of all company or to fetch data of particular company id

        Args:
            request : Get request object

        Returns:
            Response : Json data of all company or for particular company id
        """
        try:
            if pk:

                data = TEmployee.objects.get(id=pk)
                serializer = EmployeeSerializer(data)

            else:

                data = TEmployee.objects.all()
                serializer = EmployeeSerializer(data, many=True)

            return Response(serializer.data)

        except Exception as exception:
            response = HttpResponse(
                EMPLOYEE_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response

    def put(self, request: HttpRequest, pk: int) -> HttpResponse:
        """To updated the employee data for particular id

        Args:
            request : Put request object
            pk : id of employee . Defaults to None.

        Returns:
            Response : Updated data of employee for employee id
        """
        try:
            update = TEmployee.objects.get(pk=pk)
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

        except Exception as exception:
            response = HttpResponse(
                EMPLOYEE_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        """To delete employee data for particular employee id or all data of employee

        Args:
            pk : id of employee. Defaults to None.

        Returns:
            Response: message
        """
        try:
            if pk:
                delete = TEmployee.objects.get(pk=pk)
                delete.delete()

            else:
                delete = TEmployee.objects.all()
                delete.data()

            return Response({"message": "Data  Deleted Successfully"})

        except Exception as exception:
            response = HttpResponse(
                EMPLOYEE_ID_NOT_PRESENT % exception,
                status=Status.STATUS_CODE_404,
            )
            return response
