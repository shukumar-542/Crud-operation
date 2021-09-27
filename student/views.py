from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    student = Student.objects.all()
    context = {
        'student' : student 
    }

    
    return render(request, 'student/home.html', context)
