import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.1", help="The IP address of the x32 sound board")
parser.add_argument("--port", type=int, default=10023, help="The OSC port of the x32 sound board")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

# Send an OSC message to solo the first channel
message = osc_message_builder.OscMessageBuilder(address="/ch/01/config/solo")
message.add_arg(1)
client.send_message(message.build())


message = osc_message_builder.OscMessageBuilder(address="/ch/04/mix/on")
message.add_arg(0)
client.send_message(message.build())

