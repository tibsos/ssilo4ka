import os
from django.db import models as m
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from uuid import uuid4 as u4

from app.models import Block
from app.design import Theme,Background,Button,Font
from app.analytics import PageStatistics,PageActivity,ProfileActivity

def ua(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/a',s)

class Profile(m.Model):

    # DB
    uid=m.UUIDField(default=u4)
    user=m.OneToOneField(User,on_delete=m.CASCADE,related_name='profile')

    # Contact Details
    name=m.CharField(max_length=255,blank=True,null=True)
    email=m.CharField(max_length=254)

    # Profile Details
    avatar=m.ImageField(upload_to=ua)
    title=m.CharField(max_length=30,default='')
    bio=m.TextField(max_length=100,default='')

    # Industry
    category=m.ForeignKey('Category',on_delete=m.DO_NOTHING,null=True)
    subCategory=m.ForeignKey('Subcategory',on_delete=m.DO_NOTHING,null=True)
    
    # Billing
    plan=m.ForeignKey('Plan',on_delete=m.DO_NOTHING,null=True)
    
    # Security
    mfa=m.BooleanField(_("Multi-factor Authentication"),default=False)

    # Location
    ip=m.CharField(max_length=20,blank=True,null=True)
    country=m.CharField(max_length=10)
    city=m.CharField(max_length=20)

    # Начинка
    block=m.ManyToManyField(Block,blank=True,related_name='profile_blocks')

    # Appearance
    theme=m.ForeignKey(Theme,on_delete=m.DO_NOTHING,null=True)
    background=m.ForeignKey(Background,on_delete=m.DO_NOTHING,null=True)
    button=m.ForeignKey(Button,on_delete=m.DO_NOTHING,null=True)
    font=m.ForeignKey(Font,on_delete=m.DO_NOTHING,null=True)

    # Premium
    logoHidden=m.BooleanField(default=False)
    priorityLink=m.ForeignKey(Block,on_delete=m.DO_NOTHING,blank=True,null=True,related_name='profile_priority_block')
    redirectLink=m.ForeignKey(Block,on_delete=m.DO_NOTHING,blank=True,null=True,related_name='profile_redirect_block')
    
    # Activity
    statistics=m.OneToOneField(PageStatistics,on_delete=m.DO_NOTHING) 
    activity=m.ManyToManyField(ProfileActivity,blank=True)
    activity=m.ManyToManyField(PageActivity,blank=True)

    # Datetimes
    createdAt=m.DateTimeField(auto_now_add=True)
    updatedAt=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username or None
    class Meta:
        ordering=['name']

@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        a=PageStatistics.objects.create()
        Profile.objects.create(user=instance,statistics=a)
    instance.profile.save()


class Category(m.Model):
    title=m.CharField(max_length=20)
    subCategory=m.ManyToManyField('Subcategory',blank=True)
    def __str__(self):
        return self.title

class Subcategory(m.Model):
    title=m.CharField(max_length=20)
    def __str__(self):
        return self.title

class Plan(m.Model):
    title=m.CharField(max_length=255)
    price=m.PositiveSmallIntegerField(_("Price [RUB]"),)
    def __str__(self):
        return self.title

