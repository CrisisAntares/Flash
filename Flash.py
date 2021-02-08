from machine import Pin

import time

led = Pin(25, Pin.OUT)

while True:
    time.sleep(5.0)#5seconds delay
    led.value(1)#High

    time.sleep(5.0)
    led.value(0)#Low