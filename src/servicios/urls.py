from django.urls import path

from .views import (
    index,
    servicio_create,
    servicio_delete,
    servicio_detail,
    servicio_list,
    servicio_update,
)

app_name = "servicios"

urlpatterns = [
    path("", index, name="home"),
    path("servicio/list/", servicio_list, name="servicio_list"),
    path("servicio/create/", servicio_create, name="servicio_create"),
    path("servicio/update/<int:pk>", servicio_update, name="servicio_update"),
    path("servicio/detail/<int:pk>", servicio_detail, name="servicio_detail"),
    path("servicio/delete/<int:pk>", servicio_delete, name="servicio_delete"),
]
