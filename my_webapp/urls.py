from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_req, name='login'),
    path('register/', views.register_req, name='register')
]

if settings.DEBUG:
    urlpatterns = (
        urlpatterns +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
    urlpatterns = (
        urlpatterns +
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
