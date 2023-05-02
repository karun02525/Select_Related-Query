from django.contrib import admin
from .models import Employee,Deparment,Student,Teacher


admin.site.register(Employee)
admin.site.register(Deparment)

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob','age','doj','city']
    
@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary','doj','city']
    

# Register your models here.
