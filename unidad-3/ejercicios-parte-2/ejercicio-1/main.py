 # import librerias =>
import os
import platform
import typer
from rich import print

from model.cliente import Cliente


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __main():
  cliente = __createClient()
  
  while True:
    __clearConsole()
    print("[bold blue]/script cargando...[/]")

    __welcomeMessage()
    __printMenu()

    option = int(typer.prompt("   + Selecciona una opcion del menu"))

    match (option):
      case 1:
        cantidad = float(typer.prompt("  - Ingrese la cantidad que desea depositar"))
        
        if ((cliente.__depositar(cantidad)) == True):
          print("[bold green]   / Cantidad ingresada correctamente.[/]")
        else:
          print("[bold red]   / Ha ocurrido un error. No se ha podido ingresar la cantidad.[/]")
        break
      case 2:
        cantidad = float(typer.prompt("  - Ingrese la cantidad que desea retirar"))

        if ((cliente.__retirar(cantidad)) == True):
          print("[bold green]   / Cantidad retirada correctamente.[/]")
        else:
          print("[bold red]   / Ha ocurrido un error. No se ha podido retirar la cantidad.[/]")
        break
      case 3:
        print(f"[bold white]   / {cliente.__printData()}[/]")
        break
      case 4:
        print("[bold yellow] > Gracias por usar el Administrador de Recetas. Saliendo...[/]")
        exit()
    
    __waitKey();


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | welcome message | mensaje de bienvenida del programa ->
def __welcomeMessage ():
  print("[bold green] Bienvenido al Gestor de Cuenta Bancaria[/]")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | create client | permite crear un objeto cliente ->
def __createClient ():
  tempNombre = str(typer.prompt("  - Ingrese su nombre"))
  tempApellido = str(typer.prompt("  - Ingrese su apellido"))
  tempNumCuenta = int(typer.prompt("  - Ingrese su numero de cuenta"))

  return Cliente(tempNombre, tempApellido, tempNumCuenta)

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
  print("  1. Depositar una Cantidad.")
  print("  2. Retirar una Cantidad.")
  print("  3. Mostrar mis Datos.")
  print("  4. Finalizar el Programa.")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | print string | imprime en pantalla una cadena ->
def __printString (inputString):
  print(inputString)


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # save run =>
if __name__ == "__main__":
  typer.run(__main)