from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from app.urls import ssilo4ka

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('user.urls', 'user'), namespace='user')),
    path('',include('base.urls')),
    path('',include('app.urls')),
    path('blog/',include('blog.urls')),
    path('<str:username>/',ssilo4ka,name='ssilo4ka'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
