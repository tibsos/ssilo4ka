from django.urls import path
from .views import *

app_name='link'

urlpatterns=[
    path('home/',home,name='home'),
    path('design/',design,name='design'),
    path('analytics/',analytics,name='analytics'),
    path('settings/',settings,name='settings'),

    path('upgrade/select-plan',upgrade,name='upgrade'),

    #path('my-account/',my_account,name='my-account'),
    #path('billing/',billing,name='billing'),
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
    path('delete-all/',delete_all,name='delete-all'),
    path('delete-block/<uuid:uid>/',delete_block,name='delete-block'),
]
urlpatterns+=ajax_urlpatterns
urlpatterns+=htmx_urlpatterns