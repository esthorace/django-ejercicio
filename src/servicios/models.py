from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class OrdenServicio(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "Pendiente", "Pendiente"
        EN_PROCESO = "En Proceso", "En Proceso"
        COMPLETADO = "Completado", "Completado"
        CANCELADO = "Cancelado", "Cancelado"

    servicio = models.ForeignKey(
        Servicio, on_delete=models.RESTRICT, related_name="ordenes"
    )
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="ordenes"
    )
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    fecha = models.DateField()
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.PENDIENTE
    )

    def clean(self):
        from django.core.exceptions import ValidationError

        # Validación para asegurar que el presupuesto sea un valor positivo
        if self.presupuesto is not None and self.presupuesto <= 0:
            raise ValidationError(
                {"presupuesto": "El presupuesto debe ser un valor positivo."}
            )

        # Prevenir que un trabajo se maque como completado en una fecha futura
        from django.utils import timezone

        if self.estado == self.Estado.COMPLETADO and self.fecha > timezone.now().date():
            raise ValidationError(
                {
                    "estado": "No se puede marcar un trabajo como completado en una fecha futura."
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # Llama a clean() antes de guardar
        super().save(*args, **kwargs)
