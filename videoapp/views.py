from django.shortcuts import render,redirect
from django.http import HttpResponse
from videoapp.forms import UserReg
from videoapp.forms import UpdateProfile
from videoapp.forms import UpdateUser
from .forms import * 
from videoapp.models import Update,UploadFile
from epics import settings
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
import speech_recognition as sr
import os
from pydub import AudioSegment
from pathlib import Path
from pydub.silence import split_on_silence
import moviepy.editor as mp
ans_files={}
from django.core.files import File
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR,'videoapp/static/images/')
User = get_user_model()
users = User.objects.all()
# Create your views here.
def sample(r):
	return HttpResponse("<h1>Success</h1>")
def home(r):
	return render(r,'videoapp/home.html')
def about(r):
	return render(r,'videoapp/about.html')
def contact(r):
	return render(r,'videoapp/contact.html')
def register(r):
	if r.method=="POST":
		data=UserReg(r.POST)
		if data.is_valid(): 
			data.save()
			return redirect('login')
	else:
		data=UserReg()
	return render(r,'videoapp/register.html',{'data':data})

@login_required
def dashboard(r):
	return render(r,'videoapp/dashboard.html')

@login_required
def discuss(r):
	return render(r,'videoapp/discuss.html')

@login_required
def profile(r):
	return render(r,'videoapp/profile.html')

def studentjoin(r):
	return render(r,'videoapp/studentjoin.html')

def teacherjoin(r):
	return render(r,'videoapp/teacherjoin.html')

def display(request):
	User=get_user_model()
	users=User.objects.all()
	return render(request,'videoapp/display.html',{'data':users})

@login_required
def update(r):
	if r.method=="POST":
		c=UpdateUser(r.POST,instance=r.user)
		y=UpdateProfile(r.POST,r.FILES,instance=r.user.update)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			return redirect('/videoapp/profile')
	c=UpdateUser(instance=r.user)
	y=UpdateProfile(instance=r.user.update)
	return render(r,'videoapp/update.html',{'c':c,'y':y})

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('forumhome')
    context ={'form':form}
    return render(request,'videoapp/addInForum.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forumhome')
    context ={'form':form}
    return render(request,'videoapp/addInDiscussion.html',context)

def forumhome(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'videoapp/forumhome.html',context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        filename1=filename.split(".")
        if filename1[-1]=="mp4":
        	silence_based_conversion(filename,uploaded_file_url)
        answer={filename:uploaded_file_url}
        return render(request, 'videoapp/uploaddoc.html', {
            'uploaded_file_url': answer
        }) 
    return render(request, 'videoapp/uploaddoc.html')

def display_files(request):
	fs=FileSystemStorage()
	path='videoapp/static/images/'
	files_list=os.listdir(path)
	files_list.remove("images")
	files_list.remove("profile.PNG")
	files_dict={}
	for file in files_list:
		uploaded_file_url = fs.url(file)
		files_dict[file]=uploaded_file_url
	return render(request,'videoapp/display_files.html',{'files_dict':files_dict})


def delete(request):
	return HttpResponse("Deleted")


import io
def silence_based_conversion(filename,path):
	path='videoapp/static'+path
	print(path)
	clip = mp.VideoFileClip(path)
	path=path.split(".")
	print(path[0]+".wav")
	clip.audio.write_audiofile(path[0]+".wav") 
	r=sr.Recognizer()
	h=sr.AudioFile(path[0]+".wav")
	with h as source:
		r.adjust_for_ambient_noise(source)
		audio=r.record(source)
	try:
		t1=r.recognize_google(audio)
		print(t1)
		fs=FileSystemStorage()
		print(type(filename),filename)
		filename=filename.split(".")
		file=filename[0]+".txt"
		content_file=io.StringIO(t1)
		textfile=fs.save(file,File(content_file))
		return t1
	except:
		return 0