import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation




class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP20,
    )
    row_pins = (board.GP04, board.GP05, board.GP06, board.GP07)
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.RX
    rgb_pixel_pin = board.TX
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA
    led_key_pos = [24,23,18,17,10,9,36,37,44,45,50,51,
                25,22,19,16,11,8,35,38,43,46,49,52,
                26,21,20,15,12,7,34,39,42,47,48,53,
                14,13,6,33,40,41,
                2,1,0,27,28,29,3,4,5,32,31,30]
    brightness_limit = 0.5
    num_pixels = 54
    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  5,  29, 28, 27, 26, 25, 24,
     6,  7,  8,  9, 10, 11,  35, 34, 33, 32, 31, 30,
    12, 13, 14, 15, 16, 17,  41, 40, 39, 38, 37, 36,
                21, 22, 23,  47, 46, 45,
    ]
