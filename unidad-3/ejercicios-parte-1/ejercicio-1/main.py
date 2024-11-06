 # import libraries =>
import typer
from rich import print

 # main function =>
def __main ():
  firstWord = str(typer.prompt("¿Cual es tu nombre?"))
  secondWord = str(typer.prompt("Indica el nombre de tu animal favorito"))
  __createBeer(firstWord, secondWord)

 # rest functions =>
def __createBeer (firstWord, secondWord):
  print(f"[bold green] > El nombre de tu cerveza es {firstWord} {secondWord}[/]")

 # save run =>
if __name__ == "__main__":
  typer.run(__main)