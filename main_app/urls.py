"""
url.py of the commgen
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from django.urls import path
from django.views.static import serve
# from myapp.views import handler404, handler500, handler403
# from cricket.views import handler404, handler403, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cricket.urls')),

]

# handler404 = handler404
# handler403 = handler403
# handler500 = handler500

if settings.DEBUG is False:
    # urlpatterns += url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    urlpatterns += url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
else:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
