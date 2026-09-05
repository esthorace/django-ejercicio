from django.test import TestCase
from django.urls import reverse

from .forms import ClienteForm
from .models import Cliente


class ClienteCrudTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Ana Pérez",
            telefono="123456789",
            email="ana@example.com",
        )

    def test_cliente_list(self):
        response = self.client.get(reverse("servicios:cliente_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "servicios/cliente_list.html")
        self.assertContains(response, self.cliente.nombre)

    def test_cliente_create(self):
        response = self.client.post(
            reverse("servicios:cliente_create"),
            {
                "nombre": "Luis Gómez",
                "telefono": "987654321",
                "email": "luis@example.com",
            },
        )

        self.assertRedirects(response, reverse("servicios:cliente_list"))
        self.assertTrue(Cliente.objects.filter(nombre="Luis Gómez").exists())

    def test_cliente_update(self):
        response = self.client.post(
            reverse("servicios:cliente_update", args=[self.cliente.pk]),
            {
                "nombre": "Ana Actualizada",
                "telefono": "111111111",
                "email": "actualizada@example.com",
            },
        )

        self.assertRedirects(response, reverse("servicios:cliente_list"))
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nombre, "Ana Actualizada")

    def test_cliente_detail(self):
        response = self.client.get(
            reverse("servicios:cliente_detail", args=[self.cliente.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "servicios/cliente_detail.html")
        self.assertContains(response, self.cliente.email)

    def test_cliente_delete_requires_post(self):
        response = self.client.get(
            reverse("servicios:cliente_delete", args=[self.cliente.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "servicios/cliente_confirm_delete.html")
        self.assertTrue(Cliente.objects.filter(pk=self.cliente.pk).exists())

    def test_cliente_delete(self):
        response = self.client.post(
            reverse("servicios:cliente_delete", args=[self.cliente.pk])
        )

        self.assertRedirects(response, reverse("servicios:cliente_list"))
        self.assertFalse(Cliente.objects.filter(pk=self.cliente.pk).exists())

    def test_nonexistent_cliente_returns_not_found(self):
        response = self.client.get(reverse("servicios:cliente_detail", args=[9999]))

        self.assertEqual(response.status_code, 404)

    def test_cliente_form_rejects_invalid_email(self):
        form = ClienteForm({"nombre": "Cliente inválido", "email": "correo-invalido"})

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
