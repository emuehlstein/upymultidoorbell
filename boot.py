from machine import Pin
import network
from time import sleep
import uasyncio
import urequests

# WiFi Settings
ssid = "yourssidhere"
psk = "youpskhere"

# IFTTT Settings
whkey = "bZOKhSKef7BOFwVdz7EwC1"
event = "doorbell"
url = "https://maker.ifttt.com/trigger/" + doorbell + "/with/key/" + whkey

# Global doorbell settings
bt = 1    # bell time in seconds
st = 1    # strobe time in seconds

# Pin definitions
units = [
    #[id, "description", "short name", relayid, strobeid],
    ]

buttons = [
        #[id, pin, "description", "short name", t/f strobe],
        [0, 4, "Apartment 2W", "2W", False],
        [1, 10, "Apartment 2E", "2E", True],
        [2, 0, "Unit 1G", "1G", True],
        ]

relays = [
        #[id, pin, "description", "short name"],
        [0, 16, "Onboard LED", "OBL"],
        [1, 4, "Relay 2W", "R2W"],
        [2, 10, "Relay 2E", "R2E"],
        [3, 0, "Relay 1G", "R1G"],
        [4, 12, "Strobe", "STR"],
        ]

# Utility Functions

def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, psk)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig()

def initpins():
    for b in buttons:
        b.append(machine.Pin(b[1], machine.Pin.IN, machine.Pin.PULL_UP))
        print("Initilizing " + b[2] + " button on pin: " + b[1])

    for r in relays:                                                                                                                                                                
        r.append(machine.Pin(r[1], machine.Pin.IN, machine.Pin.PULL_UP))                                                                                                             
        print("Initilizing " + r[2] + " relay on pin: " + r[1]

async def ifttt_hook(buttonid):
    r = urequests.post(url, json={'value1': buttonid, 'value2': buttons[buttonid][2]})
    if response is not None and response.status_code < 400:
        print('Webhook invoked')
    else:
        print('Webhook failed') 

async def ring(relayid):
    relays[relayid][4].value(0)
    print("Passing tone on relay: " + relays[relayid][2])
    await uasyncio.sleep_ms(rt*1000)
    relays[relayid][4].value(0) 

async def flash(relayid):
    relays[relayid][4].value(0)
    print("Passing tone on relay: " + relays[relayid][2])
    await uasyncio.sleep_ms(rt*1000)
    relays[relayid][4].value(0) 

async def alloff():
    pass

