def generadorTurnos (area):
  prefijo = area[0].upper()
  numero = 1
  
  while True:
    yield f"{prefijo}-{numero}"
    numero =+ 1
  
def decoradorMensaje (function):
  def wrapper (*args, **kwargs):
    turno = function(*args, **kwargs)
    return f"Su turno es: {turno}. Espere a ser atendido."
  
  return wrapper