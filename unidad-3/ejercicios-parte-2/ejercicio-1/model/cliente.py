 # import libraries =>
from person import Persona

 # main class =>
class Cliente(Persona):
  def __init__(self, inputNombre, inputApellido, inputNumCuenta, initBalace=0):
    super().__init__(inputNombre, inputApellido)
    self.numeroCuenta = inputNumCuenta
    self.balance = initBalace

 #———————————————————————————————————————————————————————————————————————————————————————
   # rest functions =>
    # function | depositar | agrega una cantidad determinada al balance ->
  def __depositar(self, inputCantidad):
    if inputCantidad > 0:
      self.balance += inputCantidad
      return True
    else:
      return False

   #———————————————————————————————————————————————————————————————————————————————————————
    # function | retirar | eliminar una cantidad determinada al balance ->
  def __retirar(self, inputCantidad):
    if (0 < inputCantidad <= self.balance):
      self.balance -= inputCantidad
      return True
    else:
      return False
    
   #———————————————————————————————————————————————————————————————————————————————————————
    # function | printData | imprime la informacion del cliente ->
  def __printData(self):
    dataPersona = super().__printData()
    return f"{dataPersona} -> Cuenta: {self.numeroCuenta} | Saldo: {self.balance}"