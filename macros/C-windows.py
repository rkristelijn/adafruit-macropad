from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'C: Rectangle / Amethyst   ',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'L Half', [Keycode.CONTROL, Keycode.OPTION, Keycode.LEFT_ARROW]),  # Toggle and focus console (Ctrl + `)
        (0x000000, 'Alt Tab', [Keycode.COMMAND, Keycode.TAB]),  # Toggle and focus file browser (Ctrl + Shift + E)
        (0x000000, 'R Half', [Keycode.CONTROL, Keycode.OPTION, Keycode.RIGHT_ARROW]),  # Block edit down (Shift + Alt + Down)
        # 2nd row ----------
        (0x000000, 'Top L', [Keycode.CONTROL, Keycode.OPTION, Keycode.U]),  # Block edit up (Shift + Alt + Up)
        (0x000000, 'Top R', [Keycode.CONTROL, Keycode.OPTION, Keycode.I]),  # Command P (Cmd + P)
        (0x000000, 'WorkS 1', [Keycode.SHIFT, Keycode.CONTROL, Keycode.OPTION, '1']),  # Command Shift P (Cmd + Shift + P)
        # 3rd row ----------
        (0x000000, 'Down L', [Keycode.CONTROL, Keycode.OPTION, Keycode.J]),  # Format document (Alt + Shift + F)
        (0x000000, 'Down R', [Keycode.CONTROL, Keycode.OPTION, Keycode.K]),  # Find (Cmd + F)
        (0x000000, 'WS 2', [Keycode.SHIFT, Keycode.CONTROL, Keycode.OPTION, '2']),  # Replace (Cmd + Shift + H)
        # 4th row ----------
        (0x000000, 'R 2/3', [Keycode.CONTROL, Keycode.OPTION, Keycode.E]),  # Toggle line comment (Cmd + /)
        (0x000000, 'L 1/3', [Keycode.CONTROL, Keycode.OPTION, Keycode.G]),  # Fold all (Cmd + Option + Left)
        (0x000000, 'WS 3', [Keycode.SHIFT, Keycode.CONTROL, Keycode.OPTION, '3']),  # Unfold all (Cmd + Option + Right)
        # Encoder button ---
        (0x000000, 'Save', [Keycode.COMMAND, 's'])   # Save (Cmd + S)
    ]
}