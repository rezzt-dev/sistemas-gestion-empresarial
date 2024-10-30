 # import librerias =>
import os
import typer
from rich import print

from main import LEER_RECETA, CREAR_RECETA, ELIMINAR_RECETA, CREAR_CATEGORIA, ELIMINAR_CATEGORIA
from main import BASE_DIR, __printString

from model.recipeModel import __readRecipe, __createRecipe, __deleteRecipe
from model.categoryModel import __createCategory, __deleteCategory


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __executeFunctions (funcionName):
  if funcionName == LEER_RECETA:
    __listCategorys()
    nombreCategoria = str(typer.prompt("   + Introduce la categoria"))
    
    __listRecipes(nombreCategoria)
    nombreReceta = str(typer.prompt("   + Introduce la receta"))

    __readRecipe(nombreCategoria, nombreReceta)
  
  elif funcionName == CREAR_RECETA:
    __listCategorys()
    nombreCategoria = str(typer.prompt("   + Introduce la categoria"))

    nombreReceta = str(typer.prompt("   + Introduce la receta"))
    contenidoReceta = str(typer.prompt("   + Introduce el contenido de la receta"))

    __createRecipe(nombreCategoria, nombreReceta, contenidoReceta)

  elif funcionName == ELIMINAR_RECETA:
    __listCategorys()
    nombreCategoria = str(typer.prompt("   + Introduce la categoria"))
    
    __listRecipes(nombreCategoria)
    nombreReceta = str(typer.prompt("   + Introduce la receta"))

    __deleteRecipe(nombreCategoria, nombreReceta)
  
  elif funcionName == CREAR_CATEGORIA:
    __listCategorys()
    nombreCategoria = str(typer.prompt("   + Introduce la categoria"))
    __createCategory(nombreCategoria)

  elif funcionName == ELIMINAR_CATEGORIA:
    __listCategorys()
    nombreCategoria = str(typer.prompt("   + Introduce la categoria"))
    __deleteCategory(nombreCategoria)

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | list categorys | muestra una lista de las categorias disponibles ->
def __listCategorys():
  listaCategorias = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
  __printString("[bold white]  - Categorias Disponibles:" + ", ".join(listaCategorias) + "[/]")

 #———————————————————————————————————————————————————————————————————————————————————————
  # function | list recipes | muestra una lista de las recetas disponibles ->
def __listRecipes (inputCategoria):
  listaRecetas = [f for f in os.listdir(os.path.join(BASE_DIR, inputCategoria)) if f.endswith('.txt')]
  __printString("[bold white]  - Recetas disponibles:" + ", ".join(listaRecetas) + "[/]")