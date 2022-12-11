from helper import Rope
import keyboard
import time

rope = Rope(50)

rope.print()
while True:
    if keyboard.is_pressed('left') or keyboard.is_pressed('a'):
        rope.move_left()
        rope.print()
        time.sleep(.1)
    if keyboard.is_pressed('right') or keyboard.is_pressed('d'):
        rope.move_right()
        rope.print()
        time.sleep(.1)
    if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
        rope.move_up()
        rope.print()
        time.sleep(.1)
    if keyboard.is_pressed('down') or keyboard.is_pressed('s'):
        rope.move_down()
        rope.print()
        time.sleep(.1)
