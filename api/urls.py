from django.urls import path
from api import views


urlpatterns = [
    # for inserting employee data
    path("employee", views.EmployeeAPIView.as_view()),
    # for fetching all the employee data 
    path("employees/data", views.EmployeeAPIView.as_view()), 
       
    # for fetching employee data for particular id    
    # path("employee/data/<pk>", views.EmployeeAPIView.as_view()),    
    
    # for updating employee data for particular id 
    path("employee/update/<pk>", views.EmployeeAPIView.as_view()),
    # for deleting employee data
    path("employee/delete/<pk>", views.EmployeeAPIView.as_view()),
    # for inserting department data
    path("department", views.DepartmentAPIView.as_view()),
    # for inseting company
    path("company", views.CompanyAPIView.as_view()),
      
]


