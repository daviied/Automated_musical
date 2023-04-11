from flask import Flask, render_template

app = Flask(__name__)

text = "Hello, world!"

@app.route('/')
def index():
    return render_template('testing.html')

@app.route('/get')
def get():
    return text;

if __name__ == '__main__':
    app.run()
    text = text + input("enter things")

