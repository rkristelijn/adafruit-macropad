from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : '2: Navigation/Arrows',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Insert', [Keycode.INSERT]),  # Insert
        (0x000000, 'Home', [Keycode.HOME]),      # Home
        (0x000000, 'PgUp', [Keycode.PAGE_UP]),   # Page Up
        # 2nd row ----------
        (0x000000, 'Delete', [Keycode.DELETE]),  # Delete
        (0x000000, 'End', [Keycode.END]),        # End
        (0x000000, 'PgDn', [Keycode.PAGE_DOWN]), # Page Down
        # 3rd row ----------
        (0x000000, 'BackTab', [Keycode.SHIFT, Keycode.TAB]),  # Euro (assuming Alt+4 for €)
        (0x000000, 'Up', [Keycode.UP_ARROW]),                # Arrow Up
        (0x000000, 'Tab', [Keycode.TAB]),                       # X
        # 4th row ----------
        (0x000000, 'Left', [Keycode.LEFT_ARROW]),  # Left Arrow
        (0x000000, 'Down', [Keycode.DOWN_ARROW]),  # Down Arrow
        (0x000000, 'Right', [Keycode.RIGHT_ARROW]), # Right Arrow
        # Encoder button ---
        (0x000000, '', [])   # Empty encoder button
    ]
}           # REQUIRED dict, must be named 'app'    