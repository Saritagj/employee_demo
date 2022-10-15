from rest_framework import serializers
from api.serializers.company import CompanySerializer
from api.serializers.department import DepartmentSerializer
from ..models import TEmployee


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    department = DepartmentSerializer()

    class Meta:
        model = TEmployee
        fields = "__all__"