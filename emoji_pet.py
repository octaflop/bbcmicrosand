from microbit import *
import music

neutral_face = Image("20002:09090:00000:99999:00000")
thumbs_up = Image("00990:00990:99999:09999:09990")

happy_texts = [""]

music.play(music.POWER_UP)
display.show(thumbs_up)
# while True:
#     acx, acy = accelerometer.get_x(), accelerometer.get_y()
#     if acx > 10:
#         display.show(Image.HAPPY)
#     else:
#         display.show(neutral_face)
