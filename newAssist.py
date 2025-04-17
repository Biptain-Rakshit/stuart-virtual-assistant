from gtts import gTTS
from playsound import playsound


def newSpeak(x):

    text = x

    tts = gTTS(text=text, lang='en', slow=True)
    tts.save("voice2.mp3")


    # Play it (Windows)
playsound("voice1.mp3")
newSpeak("helo")
