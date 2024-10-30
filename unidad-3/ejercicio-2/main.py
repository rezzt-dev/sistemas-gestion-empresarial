 # import libraries =>
import typer
from rich import print

 # constants =>
PYTHON_WORD = "python"

 # main function =>
def __main ():
  text = str(typer.prompt("Introduce un texto")).lower()
  
  letters = []
  for i in range(3):
    letter = str(typer.prompt(f"Introduce una letra {i+1}")).lower()
    letters.append(letter)
    
  results = __createDictionary(text, letters)
  __printResults(results)

 # rest functions =>
def __searchLetters (text, letters):
  letterCounter = {}
  for letter in letters:
    counter = text.count(letter)
    letterCounter[letter] = counter
  return letterCounter

def __countWords (text):
  return len(text.split())

def __returnFirstSecondWords (text):
  words = text.split()
  return words[0], words[-1]

def __invertText (text):
  return text[::-1]

def __existsPython (text):
  return PYTHON_WORD in text

def __createDictionary (text, letters):
  countLetters = __searchLetters(text, letters)
  totalWords = __countWords(text)
  firstWord, secondWord = __returnFirstSecondWords(text)
  invertedText = __invertText(text)
  existsPython = __existsPython(text)
  
  return {
    "countLetters": countLetters,
    "totalWords": totalWords,
    "firstWord": firstWord,
    "secondWord": secondWord,
    "invertedText": invertedText,
    "existsPython": existsPython
  }
  
def __printResults (results):
  print(f"[bold green]\n > Los resultados son: [/]")
  print(f"[bold white]  - Conteo de Letras: {results['countLetters']}[/]")
  print(f"[bold white]  - Total de palabras: {results['totalWords']}[/]")
  print(f"[bold white]  - Primera palabra: {results['firstWord']}[/]")
  print(f"[bold white]  - Segunda palabra: {results['secondWord']}[/]")
  print(f"[bold white]  - Texto invertido: {results['invertedText']}[/]")
  print(f"[bold white]  - Existe Python: {results['existsPython']}[/]")

 # save run =>
if __name__ == "__main__":
  typer.run(__main)