 # main class =>
class Persona:
  def __init__(self, inputNombre, inputApellido):
    self.nombre = inputNombre
    self.apellido = inputApellido

 #———————————————————————————————————————————————————————————————————————————————————————
   # rest functions =>
    # function | printData | imprime la informacion de la persona ->
  def printData(self):
    return f"{self.nombre} | {self.apellido}"