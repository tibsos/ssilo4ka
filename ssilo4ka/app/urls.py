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
    # Blocks
    path('update-title/',update_title,name='update-title'),
    path('update-url/',update_url,name='update-url'),
    path('block-activity/',block_activity,name='block-activity'),

    path('delete-block/',delete_block,name='delete-block'),

    #Design
    path('delete-avatar/',delete_avatar,name='delete-avatar'),

    # Features
    ## Redirect

    ### Creation
    path('create-redirect-link/',create_redirect_link,name='create-redirect-link'),
    ### Updates
    path('redirect-update-time/',redirect_update_time,name='redirect-update-time'),
    path('redirect-update-date/',redirect_update_time,name='redirect-update-date'),
    path('redirect-update-timezone/',redirect_update_time,name='redirect-update-timezone'),

]

htmx_urlpatterns=[
    # Blocks
    path('add-link/',add_link,name='add-link'),
    
    path('delete-all/',delete_all,name='delete-all'),
]

urlpatterns+=ajax_urlpatterns
urlpatterns+=htmx_urlpatterns