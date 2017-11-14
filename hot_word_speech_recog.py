# -*- coding: utf-8 -*-
#!/usr/bin/env python

import speech_recognition as sr
GOOGLE_CLOUD_SPEECH_CREDENTIALS = open("credentials.json").read()

r = sr.Recognizer()

def adjust_for_ambient_noise():
	global r
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)

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

def callback():
	global r
	with sr.Microphone() as source:
		print('Waiting for Input')
		audio = r.listen(source)
		response = recognize_google(r, audio, "pt-br")
		print(response)

adjust_for_ambient_noise()

#--------------------------------------------------------

import sys
#a = open("snowboy_path.txt").read()
sys.path.append('/home/cyberlab/snowboy/swig/Python')
import snowboydecoder

import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=callback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
