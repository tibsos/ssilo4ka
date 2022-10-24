from django.contrib import admin as a
from .models import *

a.site.register(File)
a.site.register(Content)