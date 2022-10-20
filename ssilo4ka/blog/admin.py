from django.contrib import admin as a
from .models import *
a.site.register(Post)
a.site.register(Category)
