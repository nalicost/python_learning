"""website1 URL Configuration

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
from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index_view),
    path("page1/", views.page1_view),
    path("page2/", views.page2_view),
    re_path(r"^page(\d+)$", views.pagen_view),
    re_path(r"^(\d+)/(add|mul|sub)/(\d+)$", views.cal_view),
    re_path(r"^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$", views.birth_view),
    re_path(r"^birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})$", views.birth_view),
    re_path(r"^sum$", views.cal_sum_view),
    path("calculator/", views.calculater_view),
    path("tax", views.cal_tax_view),
    path("bookstore/", include("bookstore.urls")),
    path("user/", include("user.urls")),
]
