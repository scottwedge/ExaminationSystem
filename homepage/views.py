from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from login.forms import UserUpdateForm
from user.forms import ProfileUpdateForm
from user.models import Profile
from django.utils import timezone
#from .forms import addTest, testUpdate
#from .models import tests
from examination.models import CourseCourse
import logging
logger = logging.getLogger(__name__)
# Create your views here.

@login_required
def student_view(request, *args, **kwargs):
	#return HttpResponse("<h1> Welcome Student</h1>")
    logger.info('Homepage accessed')
    if request.user.profile.role == 'S':
        studentCourses = CourseCourse.objects.filter(student=request.user) 
        
        context = {
            'studentCourses' : studentCourses
        }
        
        return render(request,"student_logged_in.html",context)
    else:
        teacherCourses = CourseCourse.objects.filter(teacher=request.user) 

        context = {
            'teacherCourses' : teacherCourses
        }
        return render(request, "teacher.html", context)
	

def logout_view(request):
	logout(request)

@login_required
def changeprofile_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Welcome Student</h1>")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES,  instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('/profile')
    else:  
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
  
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, "changeprofile.html", context)

@login_required
def profile_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Welcome Student</h1>")
    return render(request, "profile.html", { })

@login_required
def grades_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Welcome Student</h1>")
    return render(request, "grades.html", { })

@login_required
def test_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Welcome Student</h1>")
    return render(request, "taketest.html", { })

@login_required
def agile_test(request, *args, **kwargs):
    #return HttpResponse("<h1> Welcome Student</h1>")
    return render(request, "ag.html", { })

