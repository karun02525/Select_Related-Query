# Select_Related-Query
python select_related('dept') query multiple table


from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Deparment,Student,Teacher
from django.db.models import Q


# Create your views here.

def home1(request):
    employees = Employee.objects.all().select_related('department')
    for emp in employees:
        print(emp.name,emp.department.name)
        
def home1(request):
    employees = Employee.objects.all().prefetch_related('department')
    for emp in employees:
        print(emp.name,emp.department.name)
        
        
        
def home(request):
    #employees = Employee.objects.all().select_related('department').all()
    #employees = Employee.objects.all().select_related('department').get(department=2)
    #employees = Employee.objects.all().select_related('department').filter(department=2)
    #employees = Employee.objects.all().select_related('department').exclude(department=2)
    #employees = Employee.objects.order_by('age')
    #employees = Employee.objects.order_by('-age')
    #employees = Employee.objects.order_by('?')
    #employees = Employee.objects.order_by('age').reverse()[:2]
    #employees = Employee.objects.values()
    #employees = Employee.objects.values('name','age')
    #employees = Employee.objects.values('age').distinct()
    #employees = Employee.objects.values_list()
    #employees = Employee.objects.values_list('id','name')
    #employees = Employee.objects.values_list('id','name',named=True)
    #employees = Employee.objects.using('default')
   
    '''' union
    qs1 = Student.objects.values_list('id','name','city',named=True)
    qs2 = Teacher.objects.values_list('id','name','city',named=True)
    student_data = qs2.union(qs1)
    '''
    
    '''' intersection
    qs1 = Student.objects.values_list('city',named=True)
    qs2 = Teacher.objects.values_list('city',named=True)
    student_data = qs1.intersection(qs2)
    '''
    
    '''' intersection
    qs1 = Student.objects.values_list('city',named=True)
    qs2 = Teacher.objects.values_list('city',named=True)
    student_data = qs2.difference(qs1)
    '''
    
    #student_data = Student.objects.filter(id=2) & Student.objects.filter(age=34)
    #student_data = Student.objects.filter(id=1,age=23)
    #student_data = Student.objects.filter(Q(id=1) & Q(age=23))

    #student_data = Student.objects.filter(id=2) | Student.objects.filter(age=44)
    #student_data = Student.objects.filter(id=1,age=23)
    #student_data = Student.objects.filter(Q(id=1) | Q(age=23))
   
    #do not return any queryset of students
    #student_data = Student.objects.get(city='pune')
    #student_data = Student.objects.get(pk=1)
    #student_data = Student.objects.first()
    #student_data = Student.objects.order_by('city').first()    
    #student_data = Student.objects.order_by('city').last()    
    #student_data = Student.objects.latest('doj')  
    #student_data = Student.objects.earliest('doj')  
    #student_data = Student.objects.all()
    #print(student_data.exists())
    
    '''Method QuerySet Method'''
    #student_data = Student.objects.create(name='radha',age=111,doj='1991-12-21',city='pusauli')
    #student_data,created = Student.objects.get_or_create(name='Muni',age=111,doj='1991-12-21',city='pusauli')
    #student_data = Student.objects.filter(id=4).update(name='Karun with priya',city='Shekhpurwa')
    #student_data, created = Student.objects.update_or_create(name='Misra',city='Gujrat',doj='1023-5-23',age=23,defaults={'name': 'Misra','city':'pusauli','age':12,'doj':'1999-12-29'})

    
    dic= {'name': 'Fimal','city':'gata','age':42,'doj':'1992-11-29'}
    ''' 
    data= [
        Student(name= 'Girs',city='delhi',age=34,doj='1991-12-9'),
        Student(name= 'Ope',city='Varanishi',age=14,doj='1993-12-9'),
        Student(name= 'Jiam',city='Gaya',age=65,doj='1997-12-9'),
        Student(name= 'Qie',city='Day',age=7,doj='1999-12-9'),
        Student(name= 'Woid',city='Bokaro',age=76,doj='1994-12-9'),
    ]    
    student_data = Student.objects.bulk_create(data)
  
  
  
    all_student_data = Student.objects.all()
    for s in all_student_data:
        s.doj='2023-05-02'
    student_data = Student.objects.bulk_update(all_student_data,['doj'])    
   
    
    #student_data = Student.objects.get(pk=22).delete()
    #student_data = Student.objects.filter(age=34).delete()
    #student_data = Teacher.objects.all().delete()
    
    student_data = Student.objects.all()
    print(student_data.count())
    
    Lookup
    '''
    #student_data = Student.objects.filter(name__exact='karun')
    #student_data = Student.objects.filter(name__iexact='karun')
    #student_data = Student.objects.filter(name__contains='karun')
    #student_data = Student.objects.filter(name__icontains='priya')
    #student_data = Student.objects.filter(id__in=[1,4,7])
    #student_data = Student.objects.filter(age__in=[23])
    #student_data = Student.objects.filter(age__gt=23)
    #student_data = Student.objects.filter(age__gte=23)
    #student_data = Student.objects.filter(age__lt=23)
    #student_data = Student.objects.filter(age__lte=23)
    #student_data = Student.objects.filter(name__startswith='p')
    #student_data = Student.objects.filter(name__istartswith='r')
    #student_data = Student.objects.filter(name__endswith='a')
    #student_data = Student.objects.filter(name__iendswith='a')
    #student_data = Student.objects.filter(doj__range=('2023-01-16','2023-04-30'))
    from datetime import date,time 
    #student_data = Student.objects.filter(dob__date=date(2023,2,2))
    #student_data = Student.objects.filter(dob__date__gt=date(2023,2,2))
    #student_data = Student.objects.filter(dob__year__lt=2022)
    #student_data = Student.objects.filter(dob__month__lte=5)
    #student_data = Student.objects.filter(dob__day=8)
    #student_data = Student.objects.filter(doj__week__gt=5)
    #student_data = Student.objects.filter(dob__week__day=2)
    #student_data = Student.objects.filter(doj__quarter=4)
    #student_data = Student.objects.filter(dob__time__gt=time(14,33,20))
    #student_data = Student.objects.filter(dob__hour__gt=4)
    student_data = Student.objects.filter(dob__isnull=True)
   

    print('****************************************************************')
    print(student_data)
    print('****************************************************************')
    print('SQL Query',student_data.query)
    print('****************************************************************')
    print('')
    print('****************************************************************')
    print('')
    print('')
    
        
    return render(request,'index.html',{'students':student_data})
        


