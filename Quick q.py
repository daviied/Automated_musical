import argparse
from pythonosc import udp_client

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.200.1", help="The IP address of the console")
parser.add_argument("--port", type=int, default=8000,help="The port number to send OSC messages")
args = parser.parse_args()

# Create an OSC client to send messages to the console
client = udp_client.SimpleUDPClient(args.ip, args.port)

# Send an OSC message to go to the next cue in the stack
client.send_message("/pb/1/30", 1)
