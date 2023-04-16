from pythonosc import udp_client

# IP address and port of the X32 mixing console
x32_ip = "192.168.0.16"
x32_port = 10023

# Create an OSC client to send messages to the X32
client = udp_client.SimpleUDPClient(x32_ip, x32_port)

# Send an OSC message to solo channel 1
#client.send_message('/ch/01/mix/on', 1)
#client.send_message('/ch/01/mix/on', 0)
#client.send_message('ch/01/mix/fader', 0.9)



class x32:
    def solo (blank, ch, state):
        if (ch < 10):
            strs = "/-stat/solosw/0" + str(ch)
        else:
            strs = "/-stat/solosw/" + str(ch)
        print(strs)
        client.send_message(strs, state)

    def mute (blank, ch, state):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/mix/on"
        else:
            strs = "/ch/" + str(ch) + "/mix/on"
        client.send_message(strs, state)

    def set_db(blank, ch, value):
        if (value >= 0):
            #temp = (value * 0.025) + 75
            temp = (5/2) * value + 75
        elif (value < -30):
            temp = (5 / 6) * (value) + 50
        elif (value >= -30 & value < 0):
            temp = (5/3) * value + 75


        temp = temp / 100
        print(temp)
        #strs = "ch/0" + str(ch) + "/mix/fader"
        client.send_message("/ch/01/mix/fader", temp)

    def change_color(self, ch, value):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/config/color"
        else:
            strs = "/ch/" + str(ch) + "/config/color"
        client.send_message(strs, value)

    def change_name(self, ch, value):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/config/name"
        else:
            strs = "/ch/" + str(ch) + "/config/name"
        client.send_message(strs, value)

    def change_icon(self, ch, value):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/config/icon"
        else:
            strs = "/ch/" + str(ch) + "/config/icon"
        client.send_message(strs, value)

    def remap(self, ch, value):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/config/source"
        else:
            strs = "/ch/" + str(ch) + "/config/source"
        client.send_message(strs, value)


    def mixbus_mute(self,ch,bus,value):
        if (ch < 10):
            strs = "/ch/0" + str(ch) + "/mix/0" + str(bus) + "/on"
        else:
            strs = "/ch/" + str(ch) + "/mix/" + str(bus) + "/on"
        client.send_message(strs, value)


    def mutegroup(self,ch,value):
        if (ch < 10):
            strs = "/config/mute/" + str(ch)
        else:
            strs = "/config/mute/" + str(ch)
        client.send_message(strs, value)

    