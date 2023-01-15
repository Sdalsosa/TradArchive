from . import views
from django.urls import path

urlpatterns = [
    path("", views.TuneList.as_view(), name="home"),
]