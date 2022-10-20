from django.urls import path
from .views import *

app_name='app'

urlpatterns=[
    path('home/',home,name='home'),
    path('design/',design,name='design'),
    path('analytics/',analytics,name='analytics'),
    #path('SEO/',seo,name='seo'),
    #path('social-icons/',social_icons,name='social-icons'),
    path('my-account/',account,name='account'),

    #path('my-account/',my_account,name='my-account'),
    #path('settings/',settings,name='settings'),
    #path('help/',help,name='help'),
]

ajax_urlpatterns=[
    path('update-title/',update_title,name='update-title'),
    path('update-url/',update_url,name='update-url'),
    path('block-activity/',block_activity,name='block-activity'),
    path('delete-avatar/',delete_avatar,name='delete-avatar'),
]

htmx_urlpatterns=[
    # links
    path('add-link/',add_link,name='add-link'),
    path('delete-block/<uuid:uid>/',delete_block,name='delete-block'),
    path('delete-all/',delete_all,name='delete-all'),
]

urlpatterns+=ajax_urlpatterns
urlpatterns+=htmx_urlpatterns