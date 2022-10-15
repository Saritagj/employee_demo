from rest_framework import serializers
from ..models import MDepartment 


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDepartment
        fields = "__all__"