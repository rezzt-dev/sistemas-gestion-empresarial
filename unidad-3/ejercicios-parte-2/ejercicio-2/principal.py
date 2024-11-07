import typer
from rich import print
from numeros import generadorTurnos, decoradorMensaje

@decoradorMensaje
def obtenerTurno (area):
  gen = generadorTurnos(area)
  return next(gen)

def __main ():
  areas = ["Optica", "Farmacia", "Cosmetica"]
  
  while True:
    print("\n[bold white] > Areas disponibles:[/]")
    for i, area in enumerate(areas, 1):
      print(f"{i}. {area}")
      
    try:
      opcion = int(typer.prompt("Selecciona el area (1-3) o 0 para salir"))
      
      if opcion == 0:
        break
      elif 1 <= opcion <= 3:
        turno = obtenerTurno(areas[opcion-1])
        print(turno)
      else:
        print("[bold yellow]  - Opcion invalida. Intente de nuevo.[/]")
    
    except ValueError:
      print("[bold red]  - Por favor, selecciona un numero valido.[/]")

if __name__ == "__main__":
  typer.run(__main)