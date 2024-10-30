 # import libraries =>
import typer
from rich import print

 # main function =>
def __main ():
  baseNumber = int(typer.prompt("Introduce un número"))
  numberSum = __sumaPrimos(baseNumber)
  print(f"[bold green] > El número suma de los números primos menores a {baseNumber} es {numberSum}[/]")

 # rest functions =>
def __sumaPrimos (number):
  def __esPrimo(n):
    if n < 2:
      return False
    
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True
  
  suma = 0
  for num in range(2, number + 1):
    if __esPrimo(num):
      suma += num
  return suma

 # save run =>
if __name__ == "__main__":
  typer.run(__main)