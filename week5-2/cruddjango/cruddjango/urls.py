"""cruddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mysites import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('postDetail/<int:post_pk>', views.postDetail, name = 'postDetail'),
    # name = 'views.py에서 호출할 함수의 이름' 은 views.py 파일에서 함수 이름을 작성하면된다.
]
