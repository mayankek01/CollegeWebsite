from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("about",views.about, name="about"),
    path("staff",views.staff, name="staff"),
    path("staffsel",views.staffsel, name="staffsel"),
    path("nonteaching",views.nonteaching, name="nonteaching"),
    path("others",views.other, name="other"),
    path("course",views.course, name="course"),
    path("notice",views.notice, name="notice"),
]
