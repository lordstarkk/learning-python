#A beginner project
#This simple program converts the text into speech using pyttsx3 module

# importing module
import pyttsx3

# defining engine
engine = pyttsx3.init()

# getting voices and speech rate
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

# setting voice and speech rate
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

# defining speak function
def speak(text):
    pyttsx3.speak(text)