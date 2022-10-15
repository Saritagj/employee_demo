from rest_framework.views import APIView
from .models import TEmployee
from rest_framework.response import Response
from api.serializers.company import CompanySerializer
from api.serializers.department import DepartmentSerializer
from api.serializers.employee import EmployeeSerializer


class EmployeeAPIView(APIView):

    def post(self, request):
        """ To insert the employee data

        Args:
            request : Post request object

        Returns:
            Response: Json of employee data
        """
        data = request.data
        serializer = EmployeeSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)
        # Create Employee in the DB
        serializer.save()

        # Return Response to User
        response = Response(serializer.data)
        return response    
    
    # def get_object(self, pk):
    #     """ To fetch employee data for particular id

    #     Args:
    #         pk : id of employee

    #     Returns:
    #         Response(Json of employee data) or raise message 
    #     """
    #     try:
    #         return TEmployee.objects.get(pk=pk)
     
    #     except TEmployee.DoesNotExist:            
    #         return Response({"message": "ID Does Not Exist"})
        
    def get(self, request):
        """ To fetch the data of all employee

        Args:
            request : Get request object

        Returns:
            Response : Json data of all employee
        """
        data = TEmployee.objects.all()
        serializer = EmployeeSerializer(data, many=True)

        return Response(serializer.data)

    def put(self, request, pk = None):
        """ To updated the employee data for particular id 

        Args:
            request : Put request object
            pk : id of employee . Defaults to None.

        Returns:
            Response : Updated data of employee for employee id
        """
        
        update = TEmployee.objects.get(pk = pk)
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

    def delete(self, pk = None):
        """ To delete employee data for particular employee id 

        Args:
            pk : id of employee. Defaults to None.

        Returns:
            Response: message
        """
        delete = TEmployee.objects.get(pk = pk)
        delete.delete()

        return Response({"message": "Data  Deleted Successfully"})


class CompanyAPIView(APIView):
    
    def post(self, request):
        """ To insert the compnay data

        Args:
            request : Post Request object

        Returns:
            Response : json data of company
        """
        data = request.data
        serializer = CompanySerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)
        # Create Company in the DB
        serializer.save()

        # Return Response to User
        response = Response(serializer.data)
        return response
    

class DepartmentAPIView(APIView):
    
    def post(self, request):
        """ TO insert data of department 

        Args:
            request : Post Request object

        Returns:
            Response : Json data of department
        """
        data = request.data
        serializer = DepartmentSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)
        # Create Department in the DB
        serializer.save()
        # Return Response to User
        response = Response(serializer.data)
        return response