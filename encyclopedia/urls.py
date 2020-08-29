from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.title,name="title"),
    path("create",views.create,name="create"),
    path("random",views.rand,name="rand"),
    path("edit/<str:title>",views.edit,name="edit"),
    path("edit",views.final,name="final")

]
