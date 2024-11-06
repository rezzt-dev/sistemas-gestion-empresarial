 # import librerias =>
import os
import platform

from main import BASE_DIR
from main import __printString


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | read recipe | muestra el contenido de una receta ->
def __readRecipe (inputCategoria, inputReceta):
  listaCategorias = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

  if inputCategoria not in listaCategorias:
    __printString("[bold red] > Categoria no encontrada.[/]")
    return
  
  listaRecetas = [f for f in os.listdir(os.path.join(BASE_DIR, inputCategoria)) if f.endswith('.txt')]

  if inputReceta not in listaRecetas:
    __printString("[bold red] > Recetas no encontrada.[/]")
    return
  
  with open (os.path.join(BASE_DIR, inputCategoria, inputReceta), 'r') as f:
    __printString(f.read())

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | create recipe | crea una receta indicando la categoria y el nombre ->
def __createRecipe (inputCategoria, inputNombre, inputContenido):
  listaCategorias = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

  if inputCategoria not in listaCategorias:
    __printString("[bold red] > Categoria no encontrada.[/]")
    return
  
  with open(os.path.join(BASE_DIR, inputCategoria, f"{inputNombre}.txt"), 'w') as f:
    f.write(inputContenido)
  __printString("[bold green] > Receta creada exitosamente.[/]")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | delete recipe | elimina una receta indicando su categoria y el nombre ->
def __deleteRecipe (inputCategoria, inputReceta):
  listaCategorias = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
  __printString("[bold white]  - Categorias Disponibles:" + ", ".join(listaCategorias) + "[/]")

  if inputCategoria not in listaCategorias:
    __printString("[bold red] > Categoria no encontrada.[/]")
    return
  
  listaRecetas = [f for f in os.listdir(os.path.join(BASE_DIR, inputCategoria)) if f.endswith('.txt')]
  __printString("[bold white]  - Recetas disponibles:" + ", ".join(listaRecetas) + "[/]")

  if inputReceta not in listaRecetas:
    __printString("[bold red] > Recetas no encontrada.[/]")
    return
  
  os.remove(os.path.join(BASE_DIR, inputCategoria, inputReceta))
  __printString("[bold green] > Receta eliminada exitosamente.[/]")