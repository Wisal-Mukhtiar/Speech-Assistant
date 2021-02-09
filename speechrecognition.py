import speech_recognition as sr
import os
import time
from gtts import gTTS
import webbrowser
import random
import playsound

r = sr.Recognizer()


def recording_sound(ask=False):
    if ask:
        felix_speak(ask)

    with sr.Microphone() as source:
        audio = r.listen(source)
        recognized_audio = ''
        try:
            recognized_audio = r.recognize_google(audio)
        except sr.UnknownValueError:
            felix_speak("I didn't get you man!")
        except sr.RequestError:
            felix_speak("Couldn't reach the server")

        return recognized_audio


def response(voice):
    if "your name" in voice:
        felix_speak("My name is Felix")
    elif "time" in voice:
        felix_speak(time.ctime())

    elif "search" in voice:
        search = recording_sound("What do you want to search for?")
        url = r'https://google.com/search?q=' + search
        webbrowser.open(url)
        felix_speak(f"Here is the result of your search for {search}")
    elif "find location" in voice:
        location = recording_sound("Which location you want to search for?")
        url = r'https://google.nl/maps/place/' + location
        webbrowser.open(url)
        felix_speak(f"Here is the location of {location} on google maps")

    elif "exit" in voice:
        felix_speak("Aye Aye captain, Have a good day")
        exit()

    else:
        felix_speak("Sir I can't get you")


def felix_speak(audio_text):
    tts = gTTS(text=audio_text, lang='en')
    ran = random.randint(1, 1000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_text)
    os.remove(audio_file)


def main():
    count = 0
    while 1:
        if count == 0:
            felix_speak("How can I help you sir?")
        else:
            time.sleep(5)
            felix_speak("How can I further assist you sir?")

        voice = recording_sound()
        response(voice)

        count += 1


main()
