from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return f'[id={self.id},name={self.name}]'


class Employee(models.Model):
    name=models.CharField(max_length=255)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=50)
    salary=models.FloatField()
    bonus=models.FloatField()

    def __str__(self):
        return f'[id={self.id},name={self.name},dept={self.dept_name},salary={self.salary},bonus={self.bonus}]'