import keyboard
import speech_recognition as sr





r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("done collecting")

text = r.recognize_google(audio)
print(text)
if (text == "close this window"):
    keyboard.press('H')
