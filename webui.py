from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)
r = sr.Recognizer()
@app.route('/')
def index():
    return render_template('GUI.html')

@app.route("/vars")
def vars():
    sent = request.args.get("vars")
    sentt = request.args.get("other")
    print(sent)
    print(sentt)

    if (sent == "detected"):
        print("hello")
        return "this is what is detected"
    if (sentt == "b"):
         return "This will be a expected cue line from the play"

@app.route("/speech")
def speech():
    speech = request.args.get("speech")

    if (speech == "a"):
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("done!")

        text = r.recognize_google(audio)
        print(text)
        return text




if __name__ == '__main__':
    app.run(port=8080)
