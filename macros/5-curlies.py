from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : '5: Brackets        ',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '(', [Keycode.LEFT_SHIFT, Keycode.NINE]),
        (0x000000, ')', [Keycode.LEFT_SHIFT, Keycode.ZERO]), 
        (0x000000, '~', [Keycode.GRAVE_ACCENT]),
        # 2nd row ----------
        (0x000000, '[', [Keycode.LEFT_BRACKET]),
        (0x000000, ']', [Keycode.RIGHT_BRACKET]),
        (0x000000, '`', [Keycode.LEFT_SHIFT, Keycode.GRAVE_ACCENT]),
        # 3rd row ----------
        (0x000000, '{', [Keycode.LEFT_SHIFT, Keycode.LEFT_BRACKET]),
        (0x000000, '}', [Keycode.LEFT_SHIFT, Keycode.RIGHT_BRACKET]),
        (0x000000, '|', [Keycode.LEFT_SHIFT, Keycode.BACKSLASH]),                         
        # 4th row ----------
        (0x000000, 'Control', [Keycode.CONTROL]),  # Empty key
        (0x000000, 'Option', [Keycode.OPTION]),  # Empty key
        (0x000000, 'Cmd', [ Keycode.COMMAND]),  # ~Command
        # Encoder button ---
        (0x000000, '', [])   # Empty encoder button
    ]
}