import os
from django.db import models as m
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from uuid import uuid4 as u4

from link.models import Block

def ua(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/a',s)

class Profile(m.Model):

    user=m.OneToOneField(User,on_delete=m.CASCADE,related_name='profile')
    name=m.CharField(max_length=255,blank=True,null=True)
    email=m.CharField(max_length=254)

    category=m.ForeignKey('Category',on_delete=m.DO_NOTHING,null=True)
    subCategory=m.ForeignKey('Subcategory',on_delete=m.DO_NOTHING,null=True)

    plan=m.ForeignKey('Plan',on_delete=m.DO_NOTHING,null=True)
    mfa=m.BooleanField(_("Multi-factor Authentication"),default=False)

    # Profile Details
    avatar=m.ImageField(upload_to=ua,blank=True,null=True)
    title=m.CharField(max_length=30,blank=True,null=True)
    bio=m.TextField(max_length=100,blank=True,null=True)

    # Начинка
    block=m.ManyToManyField(Block,blank=True,related_name='profile_blocks')

    # Appearance
    background=m.ForeignKey('Background',on_delete=m.DO_NOTHING,null=True)
    button=m.ForeignKey('Button',on_delete=m.DO_NOTHING,null=True)
    font=m.ForeignKey('Font',on_delete=m.DO_NOTHING,null=True)

    # Premium
    logoHidden=m.BooleanField(default=False)
    priorityLink=m.ForeignKey(Block,on_delete=m.DO_NOTHING,blank=True,null=True,related_name='profile_priority_block')
    redirectLink=m.ForeignKey(Block,on_delete=m.DO_NOTHING,blank=True,null=True,related_name='profile_redirect_block')

    createdAt=m.DateTimeField(auto_now_add=True)
    updatedAt=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username or None
    class Meta:
        ordering=['name']
@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
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


class Background(m.Model):

    title=m.CharField(max_length=20)

    def __str__(self):
        return self.title

class Button(m.Model):

    title=m.CharField(max_length=20)

    def __str__(self):
        return self.title

class Font(m.Model):

    title=m.CharField(max_length=20)

    def __str__(self):
        return self.title
