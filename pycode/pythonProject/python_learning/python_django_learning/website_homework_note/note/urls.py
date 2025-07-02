from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('add/', views.add_note_view),
    re_path(r'^mod/(\d+)', views.mod_note_view),
    re_path(r'^del/(\d+)', views.del_note_view),
]
