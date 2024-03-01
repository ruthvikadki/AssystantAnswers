from rest_framework import serializers
from app1.models import Department, Student

# Department serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_id', 'dept_name', 'dept_head']

# Student serializer
class StudentSerializer():
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ['std_id', 'first_name', 'last_name', 'full_name', 'department']

#Serializer for student and dept data
class StudentWithDepartmentSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Student
        fields = ['std_id', 'first_name', 'last_name', 'full_name', 'department']

