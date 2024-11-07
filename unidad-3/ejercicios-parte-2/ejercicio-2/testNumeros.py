import unittest
from numeros import generadorTurnos, decoradorMensaje

class TestGeneradorTurnos (unittest.TestCase):
  def testGeneradorOptica (self):
    gen = generadorTurnos(["Optica"])
    self.assertEqual(next(gen), "O-1")
    self.assertEqual(next(gen), "O-2")
    
  def testGeneradorFarmacia (self):
    gen = generadorTurnos(["Farmacia"])
    self.assertEqual(next(gen), "F-1")
    self.assertEqual(next(gen), "F-2")
    
  def testGeneradorCosmetica (self):
    gen = generadorTurnos(["Cosmetica"])
    self.assertEqual(next(gen), "C-1")
    self.assertEqual(next(gen), "C-2")
    

class TestDecoradorMensaje (unittest.TestCase):
  def testDecorador(self):
    @decoradorMensaje
    def funcion ():
      return "X-1"
    
    self.assertEqual(funcion(), "Su turno es: X-1. Espere a ser atendido.")
    

if __name__ == "__main__":
  unittest.main()