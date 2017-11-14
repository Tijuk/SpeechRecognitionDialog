# -*- coding: utf-8 -*-
#!/usr/bin/env python

GOOGLE_CLOUD_SPEECH_CREDENTIALS = open("credentials.json").read()

import speech_recognition as sr

r = sr.Recognizer()

def recognize_google(recognizer, audio, language):
    l = language
    text = '-=-'
    try:
        text = recognizer.recognize_google_cloud(audio, language = l, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    except sr.UnknownValueError:
        print("Google Cloud Speech não entendeu o que foi falado")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
    return text;

def adjust_amb_noise():
    global r
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

def record():
# obtain audio from the microphone
    global r
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        print("Diga algo!")
        return r.listen(source)

def listen():
    global r
    audio = record()
    return recognize_google(r, audio, "pt-br")
