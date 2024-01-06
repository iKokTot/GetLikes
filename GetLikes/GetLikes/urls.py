"""
URL configuration for GetLikes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apiGL import views
from apiGL.views import VKExchangeTokenView, GetUserAlbum,GetUserPhotos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/exchange-token/', VKExchangeTokenView.as_view(), name='exchange-token'),
    path('api/get_user_album/', GetUserAlbum.as_view(), name='user_album'),
    path('api/get_user_photos/', GetUserPhotos.as_view(), name='user_album')
]
