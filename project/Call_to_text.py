import nltk
import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("speech_recognition_test.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print(text)
