from django.contrib import admin as a
from .models import Block,Link

a.site.register(Block)
a.site.register(Link)
