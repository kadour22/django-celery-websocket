from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("index/", views.index, name="index"),
    path("dheker_by_type/<int:type_id>/", views.adhkar_by_types,name='dheker_by_type'),
    path("doaa/", views.doaa_view , name='doaa'),
    path("doaa/<int:type_id>/", views.doaa_by_type , name='doaa_type'),
    path("login/", views.login_view , name='login'),
    path("logout/", views.logout_view , name='logout'),
    path("register/", views.register_view , name='register'),
    path("tasbih/", views.tasbih , name='tasbih'),
    path("tasbih_count/", views.tasbih_view , name='tashbih_count'),
    path("reset_tasbih/", views.reset_tasbih , name='reset_tasbih'),
]
