import speech_recognition as sr
import webbrowser
import pyttsx3
import music
from openai import OpenAI
from gtts import gTTS
import time
import pygame
import os
import re




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


def openai(c):
         client = OpenAI(api_key="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")

         response = client.responses.create(
         model="gpt-4.1",
         input=c
         )

         # print(response.output_text)
         result = response.output_text
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
        openai(c)



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
        


    
    


