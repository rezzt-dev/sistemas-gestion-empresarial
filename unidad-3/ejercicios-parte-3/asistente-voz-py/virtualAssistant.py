 # import libraries ->
import pyttsx3
import speech_recognition as sr
import datetime
import requests
import os

from rich import print
from dotenv import load_dotenv

 # constants & variables ->
OPENWEATHER_API_KEY = "f890390af0e545f23382edb7645a4547"

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # load & initialize ->
load_dotenv()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

recognizer = sr.Recognizer()

#———————————————————————————————————————————————————————————————————————————————————————————————————
 # rest functions ->
  # function | audioToText | convertir una cadena de audio a texto ->
def __audioToText ():
  with sr.Microphone() as source:
    print("[bold blue] > Listening...[/]")
    
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    
  try:
    print("[bold blue] > Recognizing...[/]")
    textAudio = recognizer.recognize_google(audio, language='es-ES')
    return textAudio.lower()
  except sr.UnknownValueError:
    print("[bold red]/ERROR! Speech not Understood.[/]")
    return ''
  except sr.RequestError:
    print("[bold red]/ERROR! Could not request results from speech recognition service.[/]")
    return ''

 #————————————————————————————————————————————————————————————————————————————————————————
  # function | talk | pronunciar un mensaje utilizando texto a voz ->
def __talk(message):
  engine.say(message)
  engine.runAndWait()
  
 #————————————————————————————————————————————————————————————————————————————————————————
  # function | getCurrentTime | obtener la hora actual en formato legible ->
def __getCurrentTime ():
  now = datetime.datetime.now()
  return now.strftime("%I:%M %p")

 #————————————————————————————————————————————————————————————————————————————————————————
  # function | getCurrentDate | obtener la fecha actual en formato legible ->
def __getCurrentDate ():
  now = datetime.datetime.now()
  return now.strftime("%A, %d %B %Y")

 #————————————————————————————————————————————————————————————————————————————————————————
  # function | getWeather | obtiene informacion del clima de un ciudad concreta ->
def __getWeather(inputCity):
  apiKey = os.getenv(OPENWEATHER_API_KEY)
  baseUrl = "http://api.openweathermap.org/data/2.5/weather"
  params = {
    'q': inputCity,
    'appid': apiKey,
    'units': 'metric'
  }
  
  response = requests.get(baseUrl, params=params)
  data = response.json()
  
  if data['cod'] == 200:
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    return f"[bold green] > The temperature in {inputCity} is {temp}°C with {description}.[/]"
  else:
    return f"/ERROR! Sorry, I couldn't fetch the weather information."
