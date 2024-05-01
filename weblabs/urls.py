"""
Definition of urls for weblabs.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
import app

admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('anketa/', app.views.anketa, name='anketa'),
    path('registration/', app.views.registration, name='registration'),
    path('blog/', app.views.blog, name='blog'),
    path(r'P<parameter>/', app.views.blogpost, name='blogpost'),
    path('newpost/', app.views.newpost, name='newpost'),
    path('videopost/', app.views.videopost, name='videopost'),
    path('links/', app.views.links, name='links')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()