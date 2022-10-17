from django.urls import path
from api.views.employee import Employee
from api.views.company import Company
from api.views.department import Department


urlpatterns = [
    # for inserting employee data
    path("employee", Employee.as_view()),
    # for fetching all the employee data 
    path("employee/<pk>", Employee.as_view()), 

    # for inserting Company data
    path("company", Company.as_view()),
    # for fetching all the Company data 
    path("company/<pk>", Company.as_view()),       

    # for inserting Department data
    path("department", Department.as_view()),
    # for fetching all the Department data 
    path("department/<pk>", Department.as_view()), 


]


