 # import libraries =>
from rich import print
from rich.table import Table

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __displayResults (results: dict):
  table = Table(title="Informacion de la Pagina Web", show_header=True, header_style="bold white")
  table.add_column("Elemento", justify="left", style="green")
  table.add_column("Contenido", justify="left", style="white")
  
  for i, paragraph in enumerate(results["paragraphs"] ,1):
    table.add_row(f"Párrafo {i}", paragraph)
  
  for i, link in enumerate(results["links"], 1):
    table.add_row(f"Enlace {i}", f"Texto: {link['text']}, URL: {link['href']}")
    
  for i, header in enumerate(results["headers"], 1):
    table.add_row(f"Cabecera {i}", f"Texto: {header['text']}, Nivel: {header['level']}")

  print(table)
  
def __displayServerInfo(headers: dict):
  table = Table(title="Información del Servidor")
  table.add_column("Encabezado", justify="left", style="green")
  table.add_column("Valor", justify="left", style="white")
  
  for key, value in headers.items():
    table.add_row(key, value)
    
  print(table)
  
def __displayTechnologyInfo(sensitive_info: dict):
  # Crear una tabla para mostrar las tecnologías
  table_tech = Table(title="Tecnologías Utilizadas")
  table_tech.add_column("Tecnología", style="cyan", justify="left")
  table_tech.add_column("Categoría", style="magenta")
  table_tech.add_column("Versión", style="cyan")

  # Verificar si se ha obtenido información de las tecnologías
  if "results" in sensitive_info:
    for technology in sensitive_info["results"]:
      tech_name = technology.get("name", "Desconocido")
      tech_category = technology.get("category", "N/A")
      tech_version = technology.get("version", "N/A")
      table_tech.add_row(tech_name, tech_category, tech_version)

    print(table_tech)
  else:
    print("[bold red]Error: No se encontró información sobre tecnologías.[/bold red]")
    
  
    
    
    
    
  