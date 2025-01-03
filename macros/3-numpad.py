# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : '3: Adafruit Numpad   ', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '7', ['7']),
        (0x000000, '8', ['8']),
        (0x000000, '9', ['9']),
        # 2nd row ----------
        (0x000000, '4', ['4']),
        (0x000000, '5', ['5']),
        (0x000000, '6', ['6']),
        # 3rd row ----------
        (0x000000, '1', ['1']),
        (0x000000, '2', ['2']),
        (0x000000, '3', ['3']),
        # 4th row ----------
        (0x000000, '*', ['*']),
        (0x000000, '0', ['0']),
        (0x000000, '.', ['.']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
