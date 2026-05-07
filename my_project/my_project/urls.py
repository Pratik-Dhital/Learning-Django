"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first.views import first_fun, second_fun, contact, about_us
from vegu.views import receipe, delete_receipe, update_receipe
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', first_fun, name="first_fun"),
    path('second/', second_fun, name='second_fun'),
    path('contact/', contact, name='Contact Us'),
    path('about-us/', about_us, name='about_us'),
    path('receipe/', receipe, name='receipe'),
    path('delete-receipe/<id>/', delete_receipe, name='delete-receipe'),
    path('update-receipe/<id>/', update_receipe, name='update_receipe'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
