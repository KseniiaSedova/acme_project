from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),    
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')), 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    

