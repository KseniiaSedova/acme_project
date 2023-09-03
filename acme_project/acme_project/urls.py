from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),    
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('users.urls')),
        
]

handler404 = 'core.views.page_not_found'


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

