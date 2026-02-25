import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import OLED
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# =========================
# MATRIX CONFIGURATION
# =========================

keyboard.col_pins = (
    board.GP0,   # Column 0
    board.GP1,   # Column 1
    board.GP2,   # Column 2
    board.GP3,   # Column 3
)

keyboard.row_pins = (
    board.GP27,  # Row 1
    board.GP28,  # Row 2
    board.GP29,  # Row 3
)

# Reversed diodes
keyboard.diode_orientation = DiodeOrientation.ROW2COL


# =========================
# ENCODER CONFIGURATION
# =========================

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.GP4, board.GP6, None),  # (A, B, Switch=None)
)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]


# =========================
# OLED CONFIGURATION
# =========================

oled = OLED(
    width=128,
    height=32,
    sda=board.GP7,
    scl=board.GP26,
)

keyboard.extensions.append(oled)
keyboard.extensions.append(MediaKeys())


# =========================
# KEYMAP (3x4)
# =========================

keyboard.keymap = [
    [
        KC.ESC,    KC.N1,     KC.N2,     KC.N3,
        KC.TAB,    KC.Q,      KC.W,      KC.E,
        KC.LSFT,   KC.A,      KC.S,      KC.D,
    ]
]

if __name__ == '__main__':
    keyboard.go()