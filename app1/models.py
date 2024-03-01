from django.db import models


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True, default=0)
    dept_name = models.CharField(max_length = 20) 
    dept_head = models.CharField(max_length = 20)
    
class Student(models.Model):

    std_id = models.IntegerField(primary_key=True, default=0)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    #possibility to create ManyToMany Relationship but prioritised ForeignKey for now

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
