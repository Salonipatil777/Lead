from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.submit_photo, name='submit_photo'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
