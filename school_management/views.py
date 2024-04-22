from django.shortcuts import render
from django.views.generic import View
from data_management.models import School,SchoolClass,Subject

# Create your views here.

class SchooolsMain(View):
    def get(sefl,request):
        schools = School.objects.all()        
        return render(request,'schools.html',context={'schools':schools})
    
class ClassesMain(View):
    def get(sefl,request):
        classes = SchoolClass.objects.all()        
        return render(request,'classes.html',context={'classes':classes})
    
class SubjectsMain(View):
    def get(sefl,request):
        subjects = Subject.objects.all()        
        return render(request,'subjects.html',context={'subjects':subjects})