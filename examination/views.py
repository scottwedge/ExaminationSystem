from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import addExam, examUpdate, examInput
from .models import exam
# Create your views here.
def add_mcqs(request,*args, **kwargs):
    if request.method =='POST':
        questionaire = examInput(request.POST)
        if questionaire.is_valid():
            mcq=questionaire.save(commit=False)
            mcq.save()
            return redirect('#')
    else:
        questionaire = examInput()
    
    return render(request, 'ag.html', {'questionaire':questionaire})

def exam_detail(request, *args, **kwargs):
    element = exam.objects.all() 
    first= element[0]
    return render(request, "exam_detail.html", {'exam':first})

	#return render(request, "test_detail.html", {  })

def add_exam(request):
	#return render(request, "new_test.html", {})
	if request.method == "POST":
		form = addExam(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/exam_detail')
	else:
		form = addExam()
	
	return render(request, "add_exam.html", {'form' : form})

def edit_exam(request, pk):
    post = get_object_or_404(exam, pk=pk)
    if request.method == "POST":
        form = addExam(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('exam_detail', pk=post.pk)
    else:
        form = addExam(instance=post)
    return render(request, 'add_exam.html', {'form': form})