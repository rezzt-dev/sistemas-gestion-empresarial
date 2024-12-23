 # import libraries ->
import typer
import sys
import os
import platform
import time
import yfinance as yf
import pyjokes
import webbrowser
import wikipedia
from googletrans import Translator
from rich import print
from virtualAssistant import __talk, __audioToText, __getCurrentDate, __getCurrentTime, __searchGoogle
from virtualAssistant import GOOGLE_API_KEY, SEARCH_ENGINE_ID


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function ->
def __main ():
  __clearConsole()
  __scriptLoading()
  
  __talk("Hola! Soy SEN tu asistente personal. ¿En que puedo ayudarte?")

  while True:
    query = "buscar"  #__audioToText()
    
    if 'youtube' in query:
      __talk('Abriendo YouTube en tu Navegador Predeterminado.')
      webbrowser.open('https://www.youtube.com')
      break
    
    elif 'google' in query:
      __talk('Abriendo Google en tu Navegador Predeterminado.')
      webbrowser.open('https://www.google.com')
      break
      
    elif 'hora' in query:
      currentTime = __getCurrentTime()
      __talk(f'Son las {currentTime} actualmente.')
      break
      
    elif 'fecha' in query:
      currentDate = __getCurrentDate()
      __talk(f"Estamos a {currentDate}")
      break
    
    elif 'chiste' in query:
      chiste = pyjokes.get_joke(language='es', category='neutral')
      __talk(chiste)
      break
      
    elif 'precio acciones' in query:
      __talk('¿De que compañia te gustaria saber el precio de las acciones?')
      company = __audioToText()
      
      
      try:
        accion = yf.Ticker(company)
        price = accion.info['regularMarketPrice']
        __talk(f"El precio actual de las acciones de la compañia {company} es de {price}")
        break
      except:
        __talk('Lo siento pero no he podido encontrar informacion sobre las compañias.')
        break
    
    elif 'buscar' in query:
      __talk('¿Sobre que quieres informacion?')
      searchQuery = "Segunda Guerra Mundial" #__audioToText()
      
      try:
        results = __searchGoogle(searchQuery, GOOGLE_API_KEY, SEARCH_ENGINE_ID, num=1)
        
        if 'items' in results and results['items']:
          snippet = results['items'][0]['snippet']
          translator = Translator()
          translated_snippet = translator.translate(snippet, dest='es').text
          __talk(f"Según la búsqueda: {translated_snippet}")
          break
        
        else:
          __talk("Lo siento, no he podido encontrar información sobre ese tema.")
          break
      except Exception as ex:
        __talk(f"Ha ocurrido un error al buscar la información: {str(ex)}")
        break
        
    elif 'salir' in query or 'adios' in query:
      __talk("Adios. Que pases un buen dia.")
      break
    
  print("[bold blue] > Operacion Realizada.[/]")
  
  print("[bold white]+ Opciones Disponibles: [/]")
  print("[bold white] 1. Quiero Continuar.[/]")
  print("[bold white] 0. Salir del Programa.[/]")
  opcion = int(typer.prompt("  - Quieres continuar: (0/1)"))
  if (opcion == 1):
    __main()
  else:
    SystemExit()


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions ->
  # function | clearConsole | limpia la terminal -->
def __clearConsole():
  os.system('cls' if platform.system() == 'Windows' else 'clear') 

 #————————————————————————————————————————————————————————————————————————————————————————
  # function | welcomeMessage | mensaje de bienvenida ->
def __welcomeMessage ():
  print("[bold yellow] > Bienvenido a tu Asistente Virtual by rezzt.dev[/]")

 #————————————————————————————————————————————————————————————————————————————————————————
  # function | scriptLoading | carga del script ->
def __scriptLoading ():
  chars = "|/-\\"
  for _ in range(5):
    for char in chars:
      sys.stdout.write(f"\r{char} [script loading...]")
      sys.stdout.flush()
      time.sleep(0.1)
    
  print("\n[bold green]+ script loaded.[/]")
  __welcomeMessage


#———————————————————————————————————————————————————————————————————————————————————————————————————
 # save runner ->
if __name__ == "__main__":
  typer.run(__main)