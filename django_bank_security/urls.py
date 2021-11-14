"""django_bank_security URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from datacenter.active_passcards_view import active_passcards_view
from datacenter.passcard_info_view import passcard_info_view
from datacenter.storage_information_view import storage_information_view
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', active_passcards_view, name="active_passcards"),
    url(r'^storage_information$', storage_information_view, name="storage_information"),
    url(r'^passcard_info/(?P<passcode>[\w\-]+)/$', passcard_info_view, name="passcard_info"),
]