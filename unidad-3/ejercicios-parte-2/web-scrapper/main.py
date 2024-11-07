 # import libraries =>
import os
import platform
import typer
from rich import print

from model.scraper import __scrapeWebsite

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __main():
  __clearConsole()
  
  __loadingScript()
  __welcomeMessage()
  
  websiteUrl = str(typer.prompt(" > Introduce la URL que quieres Scrapear"))
  apiKey = "6b235d93192ed5db661c8b18f0db60bc"
  
  print("\n[bold yellow]  - Comenzando el proceso de scraping... [/]")
  __scrapeWebsite(websiteUrl, apiKey)
  
  
  
#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions =>
  # function | loadingScript | muestra un mensaje de carga -->
def __loadingScript():
  print("[bold white]/loading script...[/]")
  
   #———————————————————————————————————————————————————————————————————————————————————
  # function | welcomeMenssage | muestra un mensaje de bienvenida -->
def __welcomeMessage():
  print("[bold blue] > WebScrapper by rezzt.dev[/]")

   #———————————————————————————————————————————————————————————————————————————————————
  # function | clearConsole | limpia la terminal -->
def __clearConsole():
  os.system('cls' if platform.system() == 'Windows' else 'clear')
  
   #———————————————————————————————————————————————————————————————————————————————————
  # function |  | limpia la terminal -->
def __clearConsole():
  os.system('cls' if platform.system() == 'Windows' else 'clear')

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # function runner =>
if __name__ == "__main__":
  typer.run(__main)