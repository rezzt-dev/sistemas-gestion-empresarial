 # import libraries =>
from bs4 import BeautifulSoup
from .apiClient import __fetchContent
from .display import __displayResults, __displayServerInfo, __displayTechnologyInfo
from .sensitiveInfoExtractor import __fetchTechnologyInfo, __extractSensitiveInfo

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # main function =>
def __scrapeWebsite (url: str, api_key: str):
  response_data = __fetchContent(url, api_key)
  response_data_2 = __fetchTechnologyInfo(url)
  htmlContent = response_data["html"]
  headers = response_data["headers"]
  cookies = response_data.get("cookies", {})

  
  if not htmlContent:
    return
  
  soup = BeautifulSoup(htmlContent, "html.parser")
  results = {
    "title": soup.title.string if soup.title else "Sin título",
    "paragraphs": [p.get_text().strip() for p in soup.find_all('p')[:5]],
    "links": [{"text": a.get_text().strip(), "href": a['href']} for a in soup.find_all('a', href=True)[:5]],
    "images": [{"src": img.get('src'), "alt": img.get('alt', 'No tiene alt')} for img in soup.find_all('img')[:5]],
    "headers": [{"text": h.get_text().strip(), "level": h.name} for level in range(1, 7) for h in soup.find_all(f'h{level}')[:5]]
  }
  
  __displayResults(results)
  __displayServerInfo(headers)
  
  
  sensitive_info = __fetchTechnologyInfo(url)
  __displayTechnologyInfo(sensitive_info)
  