from django.db import models as m
from uuid import uuid4 as u4

from app.analytics import LinkActivity

from .features import RedirectLink

class Link(m.Model):
    block=m.ForeignKey('Block',on_delete=m.CASCADE,related_name='link_block',null=True)
    title=m.CharField(max_length=50,blank=True,null=True)
    activity=m.ManyToManyField(LinkActivity,blank=True)

    def __str__(self):
        return self.title or "undefined"

    class Meta:
        ordering=['title']

class Block(m.Model):


    uid=m.UUIDField(default=u4)

    active=m.BooleanField(default=True)

    url=m.CharField(max_length=3000,blank=True,null=True)
    link=m.ForeignKey(Link,on_delete=m.DO_NOTHING,null=True,related_name="blocks_link")

    to_delete=m.BooleanField(default=False)

    redirect=m.ForeignKey(RedirectLink,on_delete=m.DO_NOTHING,null=True)

    createdAt=m.DateTimeField(auto_now_add=True)
    updatedAt=m.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uid)
    class Meta:
        ordering=['-createdAt']