from django.urls import path
from django.views.generic import TemplateView

from servicios.views import *

app_name = "servicios"

urlpatterns = [
    path("", TemplateView.as_view(template_name="servicios/index.html"), name="home"),
    path("servicio/list/", servicio_list, name="servicio_list"),
    path("servicio/create/", servicio_create, name="servicio_create"),
    path("servicio/update/<int:pk>", servicio_update, name="servicio_update"),
    path("servicio/detail/<int:pk>", servicio_detail, name="servicio_detail"),
    path("servicio/delete/<int:pk>", servicio_delete, name="servicio_delete"),
    path("cliente/list/", ClienteListView.as_view(), name="cliente_list"),
    path("cliente/create/", ClienteCreateView.as_view(), name="cliente_create"),
    path("cliente/update/<int:pk>", ClienteUpdateView.as_view(), name="cliente_update"),
    path("cliente/detail/<int:pk>", ClienteDetailView.as_view(), name="cliente_detail"),
    path("cliente/delete/<int:pk>", ClienteDeleteView.as_view(), name="cliente_delete"),
]
