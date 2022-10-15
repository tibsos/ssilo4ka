from django.contrib import admin as a
from .models import Block,Link
from .design import *

a.site.register(Block)
a.site.register(Link)
a.site.register(Theme)
a.site.register(Background)
a.site.register(Button)
a.site.register(Font)
