from . import views
from django.urls import path

urlpatterns = [
    path("", views.TuneList.as_view(), name="home"),
    path("<slug:slug>/", views.TuneDetail.as_view(), name="tune_detail"),
]