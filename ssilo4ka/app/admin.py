from django.contrib import admin as a
from .models import Block,Link
from .design import *
from .analytics import *

# Blocks
a.site.register(Block)
a.site.register(Link)
# Design
a.site.register(Theme)
a.site.register(Background)
a.site.register(Button)
a.site.register(Font)
# Activity
a.site.register(PageStatistics)
a.site.register(PageActivity)
a.site.register(LinkActivity)
a.site.register(ProfileActivity)
a.site.register(Activity)
