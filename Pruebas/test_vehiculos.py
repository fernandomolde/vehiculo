import unittest
import vehiculos

class TestVehiculos(unittest.TestCase):
    
    def test_existencia(self):
        v = vehiculos.Vehiculos()
        self.assertIsNotNone(v)
    
    def test_atributos_vehiculos(self):
         v = vehiculos.Vehiculos('Toyota',180,2000)
         self.assertEqual(v.nombre,'Toyota')
         self.assertEqual(v.velocidad_max,180)
         self.assertEqual(v.kilometraje,2000)
        
    def test_todos_vehiculos_color_blanco(self):
        resp = vehiculos.Vehiculos.color
        self.assertEqual(resp,'blanco')

class Test_Bus(unittest.TestCase):
    def test_existencia_bus(self):
        b = vehiculos.Bus('Toyota',180,2000)
        self.assertEqual(b.nombre,'Toyota')
        self.assertEqual(b.velocidad_max,180)
        self.assertEqual(b.kilometraje,2000)

    def test_existencia_atributo_capacidad(self):
        b = vehiculos.Bus('Toyota',180,2000)
        b.set_capacidad(150)
        capa_b = b.capacidad
        vehiculos.Vehiculos.color = 'amarillo'
        c = vehiculos.Vehiculos()
        self.assertEqual(capa_b,150)
        self.assertEqual(c.color,'blanco')