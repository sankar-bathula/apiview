from rest_framework import serializers
from apiviewapp.models import NameModel, Employee
class NameSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=7)

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = "__all__"