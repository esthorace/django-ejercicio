from django.urls import path

from .views import index, servicio_create, servicio_list, servicio_update

app_name = "servicios"

urlpatterns = [
    path("", index, name="home"),
    path("servicio/list/", servicio_list, name="servicio_list"),
    path("servicio/create/", servicio_create, name="servicio_create"),
    path("servicio/update/<int:pk>", servicio_update, name="servicio_update"),
]
