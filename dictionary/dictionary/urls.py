"""dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from dicto import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base),
    path('index/<str:w>', views.index),
    path('index/<str:w>/<str:cat>', views.index),
    path('add/', views.add),
    path('edit/<str:eword>', views.edit),
    path('show/', views.show),
    path('delete/<str:eword>', views.delete),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)