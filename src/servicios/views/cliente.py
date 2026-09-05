from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from servicios.forms import ClienteForm
from servicios.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = "servicios/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicios/cliente_form.html"
    success_url = reverse_lazy("servicios:cliente_list")


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicios/cliente_form.html"
    success_url = reverse_lazy("servicios:cliente_list")


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "servicios/cliente_detail.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "servicios/cliente_confirm_delete.html"
    context_object_name = "cliente"
    success_url = reverse_lazy("servicios:cliente_list")
