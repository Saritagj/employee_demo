from django.http import HttpResponse , HttpRequest
from api.utils.status_code import *
from api.utils.constant import *
from rest_framework.views import APIView
from api.models import MCompany
from rest_framework.response import Response
from rest_framework import status
from api.serializers.company import CompanySerializer


class Company(APIView):
    
    def post(self, request:HttpRequest) -> HttpResponse:
        """ To insert the company data

        Args:
            request : Post Request object

        Returns:
            Response : json data of company
        """
        try:
            data = request.data
            serializer = CompanySerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create Company in the DB
            serializer.save()

            # Return Response to User
            response = Response(serializer.data)
            return response
        
        except Exception as exception:
            response = HttpResponse(
            UNEXPECTED_EXCEPTION % exception, status =  Status.STATUS_CODE_500
            )
            
            return response



    def get(self, request = HttpRequest, pk=None) -> HttpResponse:
        """ To fetch the data of all company or to fetch data of particular company id

        Args:
            request : Get request object

        Returns:
            Response : Json data of all company or for particular company id
        """
        try:
            if pk:

                data = MCompany.objects.get(id=pk)
                serializer = CompanySerializer(data)

            else:

                data = MCompany.objects.all()
                serializer = CompanySerializer(data, many=True)

            return Response(serializer.data)

        except Exception as exception:
            response = HttpResponse(
            COMPANY_ID_NOT_PRESENT % exception, Status.STATUS_CODE_404
            )
            return response

        except :
            response = HttpResponse(
            UNEXPECTED_EXCEPTION % exception, Status.STATUS_CODE_500
            )
            return response


    def put(self, request = HttpRequest, pk=None) -> HttpResponse:
        """ To updated the company data for particular id 

        Args:
            request : Put request object
            pk : id of company . Defaults to None.

        Returns:
            Response : Updated data of company for company id
        """
        try:
            update = MCompany.objects.get(pk = pk)
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
        
        except Exception as exception:
            response = HttpResponse(
            COMPANY_ID_NOT_PRESENT % exception, Status.STATUS_CODE_404
            )
            return response

        except :
            response = HttpResponse(
            UNEXPECTED_EXCEPTION % exception, Status.STATUS_CODE_500
            )
            return response

    def delete(self, request = HttpRequest, pk=None) -> HttpResponse:
        """ To delete company data for particular company id 

        Args:
            pk : id of company. Defaults to None.

        Returns:
            Response: message
        """
        try:
            if pk:
                delete = MCompany.objects.get(pk = pk)
                delete.delete()

            else:
                delete = MCompany.objects.all()
                delete.data()

            return Response({"message": "Data  Deleted Successfully"})
    
        except Exception as exception:
            response = HttpResponse(
            COMPANY_ID_NOT_PRESENT % exception, Status.STATUS_CODE_404
            )
            return response

        except :
            response = HttpResponse(
            UNEXPECTED_EXCEPTION % exception, Status.STATUS_CODE_500
            )
            return response