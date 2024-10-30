 # import librerias =>
import os
import typer
import platform
from rich import print

from controler import mainControler


#———————————————————————————————————————————————————————————————————————————————————————
 # constantes & variables =>
  # constantes metodos ->
LEER_RECETA = "muestra el contenido de una receta"
CREAR_RECETA = "crea un receta, con el nombre y el contenido"
ELIMINAR_RECETA = "elimina un receta seleccionada"

CREAR_CATEGORIA = "crea una categoria de recetas"
ELIMINAR_CATEGORIA = "eliminar una categoria de recetas"

   #——————————————————————————————————————————————————————————
  # constantes generales ->
BASE_DIR = "Recetas"


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __main():
  if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
  
  while True:
    __clearConsole()
    print("[bold blue]/script cargando...[/]")

    __welcomeMessage()
    __printMenu()

    option = int(typer.prompt("   + Selecciona una opcion del menu"))

    if option == 1:
      mainControler.__executeFunctions(LEER_RECETA)
    elif option == 2:
      mainControler.__executeFunctions(CREAR_RECETA)
    elif option == 3:
      mainControler.__executeFunctions(CREAR_CATEGORIA)
    elif option == 4:
      mainControler.__executeFunctions(ELIMINAR_RECETA)
    elif option == 5:
      mainControler.__executeFunctions(ELIMINAR_CATEGORIA)
    elif option == 6:
      __printString("[bold yellow] > Gracias por usar el Administrador de Recetas. Saliendo...[/]")
      exit()
    else:
      __printString("[bold red] > Opcion no valida. Por favor, intente de nuevo.[/]")
    
    __waitKey();


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | welcome message | mensaje de bienvenida del programa ->
def __welcomeMessage ():
  print("[bold green] Bienvenido al Administrador de Recetas[/]")
  print(f"[bold white]  - Las recetas se encuentran en: {os.path.abspath(BASE_DIR)}[/]")
  print(f"[bold white]  - Total de recetas: {__countRecipes()}[/]")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | count recipes | cuenta el numero total de recetas ->
def __countRecipes ():
  total = 0
  for _, _, archivos in os.walk(BASE_DIR):
    total += len([f for f in archivos if f.endswith('.txt')])
  
  return total

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | clear console | limpia la consola ->
def __clearConsole ():
  os.system('cls' if platform.system() == 'Windows' else 'clear')

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | wait key | espera a que se pulse enter para continuar ->
def __waitKey ():
  __printString("\n\n")
  input(" > Presiona Enter tecla para continuar...")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | print menu | muestra el menu de las operaciones disponibles ->
def __printMenu():
  print("[bold white] > Lista de Operaciones Disponibles: [/]")
  print("  1. Leer una Receta.")
  print("  2. Crear una Receta.")
  print("  3. Crear una Categoria.")
  print("  4. Eliminar una Receta.")
  print("  5. Eliminar una Categoria.")
  print("  6. Finalizar el Programa.")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | print string | imprime en pantalla una cadena ->
def __printString (inputString):
  print(inputString)


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # save run =>
if __name__ == "__main__":
  typer.run(__main)