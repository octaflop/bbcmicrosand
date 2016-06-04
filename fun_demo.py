from microbit import *
import music

"""
A short set of demos of the micropy
"""

music.play(music.POWER_UP, wait=False)
display.scroll("HELLO! I'm a micropy!")

display.scroll("You can use me to play music, and play games")

display.scroll("Try hitting the 'A' button")
while True:
    if button_a.is_pressed():
        music.play(music.PYTHON, wait=False)
        display.scroll("This is all written in python!")
        display.show(Image.SNAKE)

display.scroll("Now try hitting the 'B' button")
