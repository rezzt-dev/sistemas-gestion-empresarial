 # import libraries =>
import requests
from bs4 import BeautifulSoup
import re

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __fetchTechnologyInfo (domain:str) -> dict:
  api_key = 'cbf5b44f-4fe8-42ae-8a2d-b4a96be5a64a'

   # La URL de la API de BuiltWith
  url = f"https://api.builtwith.com/v12/api.json?key={api_key}&url={domain}"

  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    return {"error": f"No se pudo obtener información de tecnologías. Estado: {response.status_code}"}

def __extractSensitiveInfo(htmlContent: str, headers: dict, cookies: list, domain: str) -> dict:
  soup = BeautifulSoup(htmlContent, 'html.parser')
  sensitive_info = {
    "comments": [],
    "meta_tags": [],
    "javascript_variables": [],
    "endpoints": [],
    "http_headers": headers,
    "cookies": [],
    "technologies": {}
  }
  
  comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
  sensitive_info["comments"] = [comment.strip() for comment in comments]

  meta_tags = soup.find_all('meta')
  sensitive_info["meta_tags"] = [{"name": tag.get("name"), "content": tag.get("content")} for tag in meta_tags if tag.get("name")]

  js_variables = []
  scripts = soup.find_all('script')
  for script in scripts:
    if script.string:
      variables = re.findall(r'var\s+(\w+)\s*=\s*([^;]+);', script.string)
      js_variables.extend([{"variable": var[0], "value": var[1].strip()} for var in variables])

  sensitive_info["javascript_variables"] = js_variables

  endpoints = re.findall(r'https?://[^\s"\'>]+', htmlContent)
  sensitive_info["endpoints"] = endpoints

  for cookie in cookies:
    cookie_info = {
      "name": cookie.name,
      "secure": cookie.secure,
      "httponly": cookie.has_nonstandard_attr("HttpOnly"),
      "samesite": cookie.get("samesite", "None")
    }
  sensitive_info["cookies"].append(cookie_info)

  sensitive_info["technologies"] = __fetchTechnologyInfo(domain)

  return sensitive_info