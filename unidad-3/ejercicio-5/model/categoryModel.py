 # import librerias =>
import os
import platform

from main import BASE_DIR
from main import __printString


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | create category | crea una categoria de recetas introduciendo el nombre ->
def __createCategory (inputNombre):
  os.makedirs(os.path.join(BASE_DIR, inputNombre), exist_ok=True)
  __printString("[bold green] > Categoria creada exitosamente.[/]")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | delete category | elimina una categoria de recetas indicando el nombre ->
def __deleteCategory (inputCategoria):
  listaCategorias = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
  __printString("[bold white]  - Categorias Disponibles:" + ", ".join(listaCategorias) + "[/]")

  if inputCategoria not in listaCategorias:
    __printString("[bold red] > Categoria no encontrada.[/]")
    return

  os.rmdir(os.path.join(BASE_DIR, inputCategoria))
  __printString("[bold green] > Categoria eliminada exitosamente.[/]")