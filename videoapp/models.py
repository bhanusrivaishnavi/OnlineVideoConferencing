from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Update(models.Model):
	genders = [('Female','Female'),
				('Male','Male')]
	age = models.IntegerField(default=20)
	gender = models.CharField(max_length=7,choices=genders)
	image = models.ImageField(upload_to='images/profile_pics/',default='profile.PNG')
	p = models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)
def CreateProfile(sender,instance,created,**kwargs):
	if created:
		Update.objects.create(p=instance)

@classmethod
def create_from_dict(cls, d):
    return cls.objects.create()

#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    link = models.CharField(max_length=100 ,null =True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)

class UploadFile(models.Model):
    filename= models.TextField(max_length=500)
    