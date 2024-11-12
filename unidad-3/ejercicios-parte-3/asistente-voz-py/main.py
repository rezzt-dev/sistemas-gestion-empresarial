 # import libraries ->
import typer
import sys
import time
from rich import print
from virtualAssistant import *

 # main function ->
def __main ():
  __scriptLoading()
  

 # rest functions ->
  # function | welcomeMessage | mensaje de bienvenida ->
def __welcomeMessage ():
  print("[bold yellow] > Bienvenido a tu Asistente Virtual by rezzt.dev[/]")

def __scriptLoading ():
  chars = "|/-\\"
  for _ in range(20):
    for char in chars:
      sys.stdout.write(f"\r{char} [script loading...]")
      sys.stdout.flush()
      time.sleep(0.1)
    
  print("\n[bold green]+ script loaded.[/]")
  __welcomeMessage

 # save runner ->
if __name__ == "__main__":
  typer.run(__main)