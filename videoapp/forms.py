from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Update
from .models import *
from django.forms import ModelForm
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
class UserReg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"})
		}

class UpdateUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter LastName"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email"})
		}


class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Update
		fields = ['age','gender','image']
		widgets = {
		'age':forms.NumberInput(attrs={"class":"form-control"}),
		'gender':forms.Select(attrs={"class":"form-control"}),
		}

class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = [   'filename'    ]

        widgets = {'filename': forms.TextInput(attrs= {'class':'form-control', 'required': True})}
    