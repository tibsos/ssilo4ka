from django.db import models as m
from django.utils.translation import gettext_lazy as _

class Category(m.Model):
    
    t=m.CharField(_("Template name"),max_length=20)
    md=m.CharField(_("Meta Description"),max_length=160)
    s=m.SlugField(_("Slug"),max_length=100)

    def __str__(self):
        return self.t
    class Meta:
        ordering=['t']
        verbose_name='Category'

class Post(m.Model):

    c=m.ForeignKey(Category,on_delete=m.CASCADE)

    h=m.CharField(_("Template name"),max_length=50)

    mt=m.CharField(_("Meta Title"),max_length=60)
    md=m.CharField(_("Meta Description"),max_length=160)
    s=m.SlugField(_("Slug"),max_length=100)

    a=m.BooleanField(_("Active"),default=True)

    t=m.PositiveSmallIntegerField(_("Reading Time [m]"))

    p=m.DateField(_("Publish Date"),auto_now_add=True)

    def __str__(self):
        return self.mt
    class Meta:
        ordering=['-p']
        verbose_name_plural='Post'

