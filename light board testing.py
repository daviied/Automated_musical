from pythonosc import osc_message_builder
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("IP_ADDRESS_OF_CONSOLE", 7700)


msg = osc_message_builder.OscMessageBuilder(address="/fixture/1/on")
msg.add_arg(1)
client.send_message(msg.build())

msg = osc_message_builder.OscMessageBuilder(address="/playback/go/1")
client.send_message(msg.build())

msg = osc_message_builder.OscMessageBuilder(address="/playback/goTo/1/3")
client.send_message(msg.build())
