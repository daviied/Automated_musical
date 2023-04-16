from flask import Flask, render_template
from pythonosc import udp_client
from flask import Flask, render_template, request
import argparse

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.200.1", help="The IP address of the console")
parser.add_argument("--port", type=int, default=8000,help="The port number to send OSC messages")
args = parser.parse_args()

# Create an OSC client to send messages to the console
client = udp_client.SimpleUDPClient(args.ip, args.port)


@app.route('/')
def home():
    return render_template('board.html')

@app.route('/next')
def next():
    client.send_message("/pb/1/go", 1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
