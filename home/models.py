from django.db import models

# Create your models here.
class Deparment(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
    
class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    doj= models.DateField()
    department = models.ForeignKey(Deparment, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    doj= models.DateField()
    city= models.CharField(max_length=30)
    dob = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name
    
    def convert(self,obj):
        if obj is not None:
            for k,v in obj.items():
                setattr(self,k,v)
            
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    doj= models.DateField()
    salary= models.IntegerField()
    city= models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
       