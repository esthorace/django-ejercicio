from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServicioForm
from .models import Servicio


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "servicios/index.html")


def servicio_list(request: HttpRequest) -> HttpResponse:
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicio_list.html", {"servicios": servicios})


def servicio_create(request: HttpRequest) -> HttpResponse:
    form = ServicioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("servicios:home")

    return render(request, "servicios/servicio_form.html", {"form": form})


def servicio_update(request: HttpRequest, pk: int) -> HttpResponse:
    servicio = get_object_or_404(Servicio, id=pk)
    form = ServicioForm(request.POST or None, instance=servicio)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("servicios:servicio_list")

    return render(request, "servicios/servicio_form.html", {"form": form})


def servicio_detail(request: HttpRequest, pk: int) -> HttpResponse:
    servicio = get_object_or_404(Servicio, id=pk)

    return render(request, "servicios/servicio_detail.html", {"servicio": servicio})


def servicio_delete(request: HttpRequest, pk: int) -> HttpResponse:
    servicio = get_object_or_404(Servicio, id=pk)
    if request.method == "POST":
        servicio.delete()
        return redirect("servicios:servicio_list")
    return render(
        request, "servicios/servicio_confirm_delete.html", {"servicio": servicio}
    )
