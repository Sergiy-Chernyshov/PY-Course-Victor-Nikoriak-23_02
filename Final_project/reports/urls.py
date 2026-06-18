from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ppt/", views.upload_ppt_file, name="upload_ppt_file"),
    path(
        "internet-orders/",
        views.upload_internet_orders_file,
        name="upload_internet_orders_file",
    ),
]