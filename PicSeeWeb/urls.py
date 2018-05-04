"""PicSeeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from web_api.views import get_classify_list, get_album_info_list,get_server_config

urlpatterns = [
    path('admin/', admin.site.urls),
    # 请求分类列表
    path('get_classify_list', get_classify_list),
    # 请求图集列表
    path('get_album_info_list', get_album_info_list),
    # 请求配置
    path('get_server_config', get_server_config),
]
