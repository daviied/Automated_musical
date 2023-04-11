import flask
from flask import Flask, render_template, request, url_for, redirect
import speech_recognition as sr

texts = "welcome"
app = Flask(__name__)
r = sr.Recognizer()

@app.route('/')
def index():
    return render_template('Lander.html')

@app.route("/vars")
def vars():
    sent = request.args.get("vars")
    sentt = request.args.get("other")
    print(sent)
    print(sentt)

    if (sent == "detected"):
        print("hello")
        return texts
    if (sentt == "b"):
         return "This will be a expected cue line from the play"

@app.route("/speech")
def speech():
    global texts
    speech = request.args.get("speech")

    if (speech == "a"):
        with sr.Microphone() as source:
            texts = "Say Something!"
            print("say something")
            audio = r.listen(source)
            print("done")
            texts = "processing"

        text = r.recognize_google(audio)
        print(text)
        texts = text
        return text

@app.route("/get")
def get():
    return texts

@app.route("/Sound")
def sound():
    return render_template('Sound.html')

@app.route("/Lights")
def lights():
    return render_template('Lights.html')


@app.route("/lander")
def lander():
    return render_template('Lander.html')




if __name__ == '__main__':
    app.run(port=8081)
