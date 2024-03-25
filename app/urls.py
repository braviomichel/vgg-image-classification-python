from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.redirect_home),
    path('home/', views.home),
    path('home/classer/', views.get_image),
    path('home/classer/new', views.redirectio),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)