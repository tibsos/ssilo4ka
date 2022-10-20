from django.db import models as m
import os
from uuid import uuid4 as u4

# Uploads
def upload_background_image(instance,filename):
    file_extension=filename.split('.')[-1]
    file_name="%s.%s"%(u4,file_extension)
    return os.path.join('design/background/image',file_name)

def upload_background_video(instance,filename):
    file_extension=filename.split('.')[-1]
    file_name="%s.%s"%(u4,file_extension)
    return os.path.join('design/background/video',file_name)

class Theme(m.Model):
    uid=m.UUIDField(default=u4)
    title=m.CharField(max_length=20)
    premium=m.BooleanField(default=False)
    order=m.PositiveSmallIntegerField()
    background=m.ForeignKey('Background',on_delete=m.DO_NOTHING,blank=True,null=True)
    backgroundColor=m.CharField(max_length=10,blank=True,null=True)
    backgroundGradient=m.TextField(max_length=100,blank=True,null=True)
    button=m.ForeignKey('Button',on_delete=m.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['order']


class Background(m.Model):
    uid=m.UUIDField(default=u4)
    title=m.CharField(max_length=20)
    image=m.ImageField(upload_to=upload_background_image,blank=True,null=True)
    video=m.ImageField(upload_to=upload_background_video,blank=True,null=True)

    def __str__(self):
        return self.title

class Button(m.Model):
    uid=m.UUIDField(default=u4)
    title=m.CharField(max_length=20)
    css=m.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Font(m.Model):
    uid=m.UUIDField(default=u4)
    title=m.CharField(max_length=20)
    css=m.TextField(max_length=1000)

    def __str__(self):
        return self.title