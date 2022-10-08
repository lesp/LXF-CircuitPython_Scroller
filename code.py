import rotaryio
import board
import time
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
encoder = rotaryio.IncrementalEncoder(board.GP17, board.GP16)
button = DigitalInOut(board.GP15)
button.direction = Direction.INPUT
button.pull = Pull.UP
last_position = 0

while True:
    position = encoder.position
    if position > last_position:
        print(position)
        mouse.move(wheel=1)
        time.sleep(0.1)
    elif position < last_position:
        print(position)
        mouse.move(wheel=-1)
        time.sleep(0.1)
    elif button.value == 0:
        print("Pressed")
        kbd.send(Keycode.PRINT_SCREEN)
        time.sleep(0.2)
    last_position = position

