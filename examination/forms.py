from django import forms
from .models import exam, MultipleChoice


class addExam(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder': 'Add Test Title...',
			'style': 'font-size: 24px;',
		}
	))
	question = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter a Question',
			

		}
	))
	option1 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Option1',
			
		}
	))
	option2 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Option2',
			
		}
	))
	option3 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Option3',
			
		}
	))
	option4 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Option4',
			
		}
	))
	
	correct = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Re-enter the correct answer',
			

		}
	))

	class Meta:
		model = exam
		fields = ('title','question','option1','option2','option3','option4','correct')

class examUpdate(forms.ModelForm):
	title = forms.CharField(label = 'Title')
	question = forms.CharField(label='Question')
	option1 = forms.CharField(label='Option1')
	option2 = forms.CharField(label='Option2')
	option3 = forms.CharField(label='Option3')
	option4 = forms.CharField(label='Option4')
	correct = forms.CharField(label='Correct')

	class Meta:
		model = exam
		fields = ('title','question','option1','option2','option3','option4','correct')

#CHOICES = ['answer1','answer2','answer3','answer4']
class examInput(forms.ModelForm):
	widget = forms.RadioSelect(choices=['one','two','answer3','answer4'])
	big = forms.CharField(label='bbbb')
	class Meta:
		model = MultipleChoice
		fields = ('answer1','answer2','answer3','answer4')



