from microbit import *
import radio

radio.enable(32, 4)

HEADER = b'\xff'
rdo_ON = HEADER + b'\x01'
rdo_OFF = HEADER + b'\x00'

while True:
    is_pressed = button_a.is_pressed()
    if is_pressed:
        radio.send(rdo_ON)
    else:
        radio.send(rdo_OFF)
    was_pressed = is_pressed
    rec = radio.recv()
    if rec == rdo_ON:
        display.show(Image("00000:00000:00909:00000:00000"))
    elif rec == rdo_OFF:
        display.clear()
    sleep(5)
