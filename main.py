import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import google.generativeai as genai
from gtts import gTTS
import time
import pygame
import os
import re
from dotenv import load_dotenv



load_dotenv()


recognixer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


# def speak(x):

#     # Clean the input text to remove unwanted characters
#     cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', x)

#     # Save the speech to an MP3 file
#     tts = gTTS(x,slow=False)
#     tts.save("voice3.mp3")

#     # Initialize and play using pygame
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load("voice3.mp3")
#     pygame.mixer.music.play()

#     # Wait until the audio finishes
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("voice3.mp3")




def gemini(c):
        
        # use gemini model
        api_key = os.getenv('api_key')

        genai.configure(api_key=api_key)

        # Use a valid model from your list
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

        # Ask something
        response = model.generate_content(c)

        result = response.text
        speak(result)



def processCommand(c):

    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com/")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://www.facebook.com/")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com/")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://www.linkedin.com/")

    elif("play" in c.lower()):
        song = c.lower().split(" ")[1]
        link = music.music[song]
        webbrowser.open(link)
    
    else:
        # let handle Open ai
        gemini(c)



if __name__ == "__main__":
    
    speak("Initializing Stuart...")

    # obtain audio from the microphone
    
    while True:

        
        # recognize speech using google
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=1)

            print("Recognizing...")
            word = r.recognize_google(audio)
            # print(word)
            if("stuart" in word.lower()):
                
                speak("yaa")

                #listen for command
                with sr.Microphone() as source:
                    print("stuart active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)


                processCommand(command)

        except Exception as e:
            print("Error")
        


    
    


