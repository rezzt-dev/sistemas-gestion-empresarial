 # import libraries =>
import typer
import random
from rich import print

 # main function =>
def __main ():
  userName = str(typer.prompt("Introduce tu nombre"))
  print(f"[bold green] > Bueno, {userName}, he pensado un numero entre 1 y 100[/]")
  
  secretNumber = __generateRandomNumber()
  numbersTry = 8
  
  for intento in range(1, numbersTry + 1):
    try:
      numberUser = int(typer.prompt(f"   + Intento {intento}: Introduce tu numero"))
      
      if not __validateNumber(numberUser):
        print("[bold red] > Has elegido un número que no está permitido. Debe ser entre 1 y 100.[/]")
        continue
      
      result = __compareNumbers(numberUser, secretNumber)
      print(result)
      
      if numberUser == secretNumber:
        print(f"[bold green] > Has ganado en {intento} intentos![/]")
        return
      
    except ValueError:
      print("[bold red] > El número debe ser un número entero.[/]")
  
  print(f"[bold red] > Lo siento, has agotado tus {numbersTry} intentos. El número secreto era {secretNumber}.[/]")

 # rest functions =>
def __generateRandomNumber ():
  return random.randint(1, 100)

def __validateNumber (number):
  return 1 <= number <= 100

def __compareNumbers (numberUser, secretNumber):
  if numberUser < secretNumber:
    return f"[bold red]  - Numero incorrecto, el secreto es mayor[/]"
  elif numberUser > secretNumber:
    return f"[bold red]  - Numero incorrecto, el secreto es menor[/]"
  else:
    return f"[bold green]  - Numero correcto[/]"

 # save run =>
if __name__ == "__main__":
  typer.run(__main)