from django.db import models as m

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

class Profile(m.Model):

    user=m.ForeignKey(User,on_delete=m.CASCADE)
    name=m.CharField(max_length=200,blank=True,null=True)

    plan=m.ForeignKey('Plan',on_delete=m.DO_NOTHING)

    mfa=m.BooleanField(_("Multi-factor Authentication"),default=False)

    category=m.ForeignKey('Category',on_delete=m.DO_NOTHING)
    subcategory=m.ForeignKey('Subcategory',on_delete=m.DO_NOTHING)

    created_at=m.DateTimeField(auto_now_add=True)
    updated_at=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username or None
    class Meta:
        ordering=['name']

class Plan(m.Model):
    title=m.CharField(max_length=255)
    price=m.PositiveSmallIntegerField(_("Price [RUB]"),)
    def __str__(self):
        return self.title

class Category(m.Model):
    title=m.CharField(max_length=20)
    def __str__(self):
        return self.title

class Subcategory(m.Model):
    parent=m.ForeignKey(Category,on_delete=m.CASCADE)
    title=m.CharField(max_length=20)
    def __str__(self):
        return self.title


@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
