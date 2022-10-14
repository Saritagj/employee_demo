from . import views
from django.urls import path


urlpatterns = [
    path("employee/", views.EmployeeAPIView.as_view()),
    path("employee/<pk>", views.EmployeeAPIView.as_view()),
    path("employee/update/<pk>", views.EmployeeAPIView.as_view()),
    path("employee/delete/<pk>", views.EmployeeAPIView.as_view()),
    path("department/", views.DepartmentAPIView.as_view()),
    path("company/", views.CompanyAPIView.as_view()),
    path("company/update/<pk>", views.CompanyAPIView.as_view()),
]
