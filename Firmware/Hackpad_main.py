import board
import digitalio
import rotaryio
import usb_hid
from kmk.kmktime import get_ticks_ms
from kmk.keys import KC
from kmk.macros import simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.led import RGBMatrix
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.sequences import send_sequence
from kmk.hid import ConsumerControlCode, MouseKeySubAction
from kmk.kmkpy import KMKKeyboard

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

# Assume 3x4 matrix: rows GP2, GP3, GP4; cols GP5, GP6, GP7, GP8
keyboard.matrix = [
    [KC.N1, KC.N2, KC.N3, KC.N4],
    [KC.N5, KC.N6, KC.N7, KC.N8],
    [KC.N9, KC.N0, KC.BS, KC.ENT],
]
# Cols to rows: cols = [board.GP5, board.GP6, board.GP7, board.GP8]
# rows = [board.GP2, board.GP3, board.GP4]
keyboard.col_pins = (5,6,7,8)
keyboard.row_pins = (2,3,4)
keyboard.matrix_type = "ROWS"

# Encoder: assume A=GP1, B=GP0, button=GP9
enc_handler = EncoderHandler()
enc_handler.pins = ((0, 1, 9),)
enc_handler.on_clockwise_do(lambda: keyboard.consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT))
enc_handler.on_counter_clockwise_do(lambda: keyboard.consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT))
enc_handler.on_click_do(lambda: keyboard.consumer_control.send(ConsumerControlCode.MUTE))
keyboard.modules.append(enc_handler)

# Optional RGB under keys, assume D4-D11 or something, but for simplicity skip or configure if pins match
# rgb_matrix = RGBMatrix(
#     led_pin=board.NEOPIXEL? or whatever,
#     num_leds=12,  # 12 keys
#     val_range=(0, 50),
#     ...
# )
# keyboard.modules.append(rgb_matrix)

if __name__ == '__main__':
    keyboard.go()
