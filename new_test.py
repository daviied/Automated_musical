from pythonosc import udp_client

# IP address and port of the X32 mixing console
x32_ip = "192.168.10.37"
x32_port = 10023

# Create an OSC client to send messages to the X32
client = udp_client.SimpleUDPClient(x32_ip, x32_port)

# Send an OSC message to solo channel 1
#client.send_message('/ch/01/mix/on', 1)
client.send_message('/ch/01/mix/fader', 0.5)


