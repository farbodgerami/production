from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
     path('',TemplateView.as_view(template_name="index.html")),
    path('api/users/', include('users.urls')),
    path('api/le504/', include('le504.urls')),
    path('api/le1100/', include('le1100.urls')),
    path('api/le800/', include('le800.urls')),
    path('api/le3500/', include('le3500.urls')),
    path('api/lecollins/', include('collins.urls')),
    path('api/lebarrens/', include('barrens.urls')),
    path('ckeditor/', include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
