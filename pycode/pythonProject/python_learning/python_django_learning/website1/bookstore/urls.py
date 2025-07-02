from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index_view),
    re_path(r"mod/(\d+)", views.modify_view),
    path(r"add/", views.add_view),
    re_path(r"del/(\d+)", views.del_view),
    path("filter/", views.filter_view),
]