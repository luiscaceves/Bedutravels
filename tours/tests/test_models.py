from django.test import TestCase

from tours.models import Zona


class ZonaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Zona.objects.create(
            nombre="Zona de prueba",
            descripcion="Descripción de la zona de prueba"
        )

    def test_nombre_etiqueta(self):
        zona = Zona.objects.get(id=1)
        nombre_etiqueta = zona._meta.get_field('nombre').verbose_name
        self.assertEqual(nombre_etiqueta, "nombre")

    def test_nombre_max_length(self):
        zona = Zona.objects.get(id=1)
        nombre_max_length = zona._meta.get_field('nombre').max_length
        self.assertEqual(nombre_max_length, 45)

