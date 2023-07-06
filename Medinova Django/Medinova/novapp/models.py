from django.db import models

# Create your models here.
dept_list=[
    ('Neurology','Neurology'),
    ('Dental','Dental'),
    ('Surgery','Surgery'),
    ('Cardiology','Cardiology'),
    ]
doctor_list=[
    ('Mr. Prakash','Mr. Prakash'),
    ('Mrs. Neha','Mrs. Neha'),
    ('Mr. Dewan','Mr. Dewan'),
    ('Mr. Rahul','Mr. Rahul'),
    ]
class Appoinment(models.Model):
    department=models.CharField(max_length=200,choices=dept_list)
    doctor=models.CharField(max_length=200,choices=doctor_list)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    