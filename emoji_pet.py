from microbit import *
import music

neutral_face = Image("09090:00000:99999:00000:00000")
grin_face = Image("09090:00000:90009:09990:00000")
happy_face = Image("09090:00000:99999:90009:09990")

frowning_face = Image("09090:00000:09990:90009:00000")
sad_face = Image("09090:00000:09990:90009:90009")

thumbs_up = Image("00990:00990:99999:09999:09990")

happy_texts = [""]

music.play(music.POWER_UP, wait=False)
# while True:
acx, acy = accelerometer.get_x(), accelerometer.get_y()


def animate(faces, delay=500):
    for face in faces:
        display.show(face)
        sleep(delay)


def get_happy(loops=2):
    music.play(music.BA_DING, wait=False)
    for i in range(loops):
        animate([neutral_face, grin_face, happy_face])


def get_sad(loops=2):
    music.play(music.POWER_DOWN, wait=False)
    for i in range(loops):
        animate([neutral_face, frowning_face, sad_face])

while True:
    get_sad(loops=100)
