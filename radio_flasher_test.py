from microbit import *
import radio

radio.enable(32, 4)

HEADER = b'\xff'
rdo_ON = HEADER + b'\x01'
rdo_OFF = HEADER + b'\x00'

was_pressed = False
while True:
    is_pressed = button_a.is_pressed()
    if is_pressed is not was_pressed:
        if is_pressed is True:
            radio.send(rdo_ON)
        else:
            radio.send(rdo_OFF)
    was_pressed = is_pressed
    rec = radio.recv()
    if rec == rdo_ON:
        display.show(Image("12345:67898:76543:21012:34567"))
    elif rec == rdo_OFF:
        display.clear()
    sleep(5)
