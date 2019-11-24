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
from examination.models import CourseCourse, exam, MultipleChoice
from examination.forms import CreateExamForm, CreateQuestionForm
from course.forms import CourseCreationForm, AddExamToCourseForm
from django.contrib.auth.models import User

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
    studentCourses = CourseCourse.objects.filter(student=request.user) 
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
        'p_form' : p_form,
        'studentCourses' : studentCourses
    }
    return render(request, "changeprofile.html", context)

@login_required
def profile_view(request, *args, **kwargs):
    studentCourses = CourseCourse.objects.filter(student=request.user) 
        
    context = {
        'studentCourses' : studentCourses
    }

    return render(request, "profile.html", context)

@login_required
def grades_view(request, *args, **kwargs):
    studentCourses = CourseCourse.objects.filter(student=request.user) 
        
    context = {
        'studentCourses' : studentCourses
    }
    return render(request, "grades.html", context)

@login_required
def agile_test(request, exam_id, *args, **kwargs):
    studentCourses = CourseCourse.objects.filter(student=request.user) 
    mcquestions = MultipleChoice.objects.filter(exam_name=exam_id)
    user = User.objects.get(username=request.user)
    context = {
        'studentCourses' : studentCourses,
        'mcquestions' : mcquestions,
        'user':user,
    }

    return render(request, "ag.html", context)

@login_required
def course_exams_view(request, course_id, *args, **kwargs):
    studentCourses = CourseCourse.objects.filter(student=request.user)
    courses = CourseCourse.objects.filter(student=request.user).filter(id=course_id) 

    context = { 
        'courses': courses,
        'studentCourses' : studentCourses
     }

    return render(request, "course_exams.html", context)

@login_required
def course_grades_view(request, course_id, *args, **kwargs):
    studentCourses = CourseCourse.objects.filter(student=request.user)
    courses = CourseCourse.objects.filter(student=request.user).filter(id=course_id) 

    context = { 
        'courses': courses,
        'studentCourses' : studentCourses
     }

    return render(request, "course_grades.html", context)

@login_required
def add_course_view(request, *args, **kwargs):
    logger.info('Add course accessed')
    if request.user.profile.role == 'T':
        if request.method == 'POST':
            add_form = CourseCreationForm(request.POST)

            if add_form.is_valid:
                add_form.save()
            return redirect('/homepage')
        else:  
            add_form = CourseCreationForm()
    
        context = {'add_form' : add_form }
        
        return render(request,"add_course.html",context)
    else:
        return redirect('/')

@login_required
def apply_exam_view(request, course_id, *args, **kwargs):
    logger.info('Apply exam accessed')
    course = CourseCourse.objects.filter(teacher=request.user).filter(id=course_id).first()
    if request.user.profile.role == 'T':
        if request.method == 'POST':
            add_form = AddExamToCourseForm(request.POST, request.FILES, instance=course)

            if add_form.is_valid:
                add_form.save()
            return redirect('/homepage')
        else:  
            add_form = AddExamToCourseForm(instance=course)
    
        context = {'add_form' : add_form }
        
        return render(request,"course_apply_exam.html",context)
    else:
        return redirect('/')        

@login_required
def add_exam_view(request, *args, **kwargs):
    logger.info('Create exam accessed')
    
    if request.user.profile.role == 'T':
        if request.method == 'POST':
            add_form = CreateExamForm(request.POST)

            if add_form.is_valid:
                add_form.save()
            return redirect('/add_exam_question')
        else:  
            add_form = CreateExamForm()
    
        context = {'add_form' : add_form }
        
        return render(request,"add_exam.html",context)
    else:
        return redirect('/')           

@login_required
def add_exam_question_view(request, *args, **kwargs):
    logger.info('Create exam accessed')
    
    if request.user.profile.role == 'T':
        if request.method == 'POST':
            add_form = CreateQuestionForm(request.POST)

            if add_form.is_valid:
                add_form.save()
            return redirect('/add_exam_question')
        else:  
            add_form = CreateQuestionForm()
    
        context = {'add_form' : add_form }
        
        return render(request,"add_exam_question.html",context)
    else:
        return redirect('/')  

@login_required
def teacher_grading_course_view(request, *args, **kwargs):
    logger.info('Teacher Course Grading accessed')
    
    if request.user.profile.role == 'T':
                
        return render(request,"teacher_grading_course.html",context)
    else:
        return redirect('/')


@login_required
def teacher_grading_student_view(request, *args, **kwargs):
    logger.info('Teacher Student Grading accessed')
    
    if request.user.profile.role == 'T':
        
        
        return render(request,"student_grading_course.html",context)
    else:
        return redirect('/')        