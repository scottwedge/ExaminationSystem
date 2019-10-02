from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def student_view(request, *args, **kwargs):
	#return HttpResponse("<h1> Welcome Student</h1>")
		return render(request, "student_logged_in.html", { })
	

def logout_view(request):
	logout(request)

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

