from django.contrib import admin

from .models import Cliente, OrdenServicio, Servicio

admin.site.register(Servicio)
admin.site.register(Cliente)


@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente",
        "servicio",
        "fecha",
        "presupuesto",
        "estado",
        "pagado",
    )
    list_filter = ("estado", "fecha", "servicio", "pagado")
    search_fields = ("cliente__nombre", "servicio__nombre")
    date_hierarchy = "fecha"

    # Agrupación visual
    fieldsets = (
        (
            "Información del Cliente y Servicio",
            {
                "fields": ("cliente", "servicio"),
            },
        ),
        (
            "Detalles del Servicio",
            {
                "fields": ("fecha", "presupuesto", "estado", "pagado"),
            },
        ),
    )
