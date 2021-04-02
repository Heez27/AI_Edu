"""django_practices URL Configuration

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

#참고: http://localhost:9999/ 로 접속
#ex. http://localhost:9999/admin
from django.contrib import admin
from django.urls import path

import helloworld.views as helloworldviews #코드에 alias(helloworldvuews)로 이용

urlpatterns = [
    path('hello1/', helloworldviews.hello1),
    path('hello2/', helloworldviews.hello2),
    path('admin/', admin.site.urls)
]
