
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from app1.models import Department, Student
from .serializers import DepartmentSerializer, StudentSerializer

#Viewset for department
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

#Restricting access to viewsets, we use IsAuthenticated
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return permission_classes

#Student Viewset
class StudentWithDepartmentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Add student with dept
    def create(self,request, *args, **kwargs):
        dept_data = request.data.get('department')

        if dept_data:
            try:
                department, created = Department.objects.get_or_create(**dept_data)
            except Exception as e:
                return Response('error 404')
            
            student = super().create(request, *args, **kwargs)
            student.departments.add(department)
            student.save()
            return Response(StudentSerializer(student).data)
        else:
            return super().create(request, *args, **kwargs)
    
#Update student with dept   
    def update(self,request,*args,**kwargs):
        dept_data = request.data.get('department')

        if dept_data:
            try:
                department, created = Department.objects.get_or_create(**dept_data)
            except Exception as e:
                return Response('error 404')
            
            student = self.get_object()
            student.departments.clear()  # Clear existing departments
            student.departments.add(department)
            student.save()
            return Response(StudentSerializer(student).data)
        else:
            return super().update(request, *args, **kwargs)
        
#Retrieve student details
    def retrieve(self,request,*args,**kwargs):
        try:
            student = self.get_object()
        except Exception as e:
            raise ValidationError("Cannot Retrieve Student Details") 
                 
#delete student       
    def delete(self,request,*args,**kwargs):
        student = self.get_object()
        student.departments.clear()
        student.delete()

        return Response("No Content Available")


