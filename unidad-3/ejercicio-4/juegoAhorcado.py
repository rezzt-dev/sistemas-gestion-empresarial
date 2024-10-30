 # import libraries =>
import typer
import random
from rich import print

 # constants & variables =>
listWords = ["pithon", "programacion", "computadora", "juego", "desarrollo"]

 # main function =>
def __main ():
  word = __selectWord()
  letrasAdivinadas = set()
  
  vidas = 6
  
  print(f"[bold green] > Bienvenido al juego del Ahorcado[/]")
  print(__mostrarTablero(word, letrasAdivinadas))
  
  while True:
    letra = str(typer.prompt(" > Elige una letra")).lower()
    
    if letra in letrasAdivinadas:
      print("[bold red]  - Ya has intentado esa letra. Prueba con otra.[/]")
      continue
    
    letrasAdivinadas.add(letra)
    
    if letra in word:
      print(f"[bold green]  - Correcto[/]")
    else:
      vidas -= 1
      print(f"[bold red]  - Incorrecto. Te quedan {vidas} vidas.[/]")
    
    tablero = __mostrarTablero(word, letrasAdivinadas)
    print(tablero)
    
    if "_" not in tablero:
      print(f"[bold green] > Felicidades! Has ganado. La palabra era: {word}[/]")
      break
    
    if vidas == 0:
      print(f"[bold red] > Lo siento, has perdido. La palabra era: {word}[/]")
      break
  

 # rest functions =>
def __selectWord ():
  return random.choice(listWords)

def __mostrarTablero(word, letrasAdivinadas):
  result = []
  for letra in word:
    if letra in letrasAdivinadas:
      result.append(letra)
    else:
      result.append('_')
    
  return ''.join(result)

 # save run =>
if __name__ == "__main__":
  typer.run(__main)