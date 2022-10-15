from rest_framework import serializers
from ..models import MCompany


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MCompany
        fields = "__all__"
