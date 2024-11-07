 # import libraries =>
import os
import requests
import platform
import typer
from rich import print

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __fetchContent (url: str, api_key: str) -> dict:
  apiUrl = f"http://api.scraperapi.com?api_key={api_key}&url={url}"
  response = requests.get(apiUrl)
  
  if response.status_code == 200:
    return {"html": response.text, "headers": response.headers}
  else:
    print(f"[bold red]\n > Error: No se pudo obtener el contenido de {url}[/]")
    return {"html": "", "headers": {}}