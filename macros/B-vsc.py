from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'B: Visual Studio Code',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Cons', [Keycode.CONTROL, Keycode.GRAVE_ACCENT]),  # Toggle and focus console (Ctrl + `)
        (0x000000, 'Files', [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]),  # Toggle and focus file browser (Ctrl + Shift + E)
        (0x000000, 'BlkDn', [Keycode.SHIFT, Keycode.ALT, Keycode.DOWN_ARROW]),  # Block edit down (Shift + Alt + Down)
        # 2nd row ----------
        (0x000000, 'BlkUp', [Keycode.SHIFT, Keycode.ALT, Keycode.UP_ARROW]),  # Block edit up (Shift + Alt + Up)
        (0x000000, 'CmdP', [Keycode.COMMAND, 'p']),  # Command P (Cmd + P)
        (0x000000, 'CmdShP', [Keycode.COMMAND, Keycode.SHIFT, 'p']),  # Command Shift P (Cmd + Shift + P)
        # 3rd row ----------
        (0x000000, 'Fmt', [Keycode.ALT, Keycode.SHIFT, 'f']),  # Format document (Alt + Shift + F)
        (0x000000, 'Find', [Keycode.COMMAND, 'f']),  # Find (Cmd + F)
        (0x000000, 'Repl', [Keycode.COMMAND, Keycode.SHIFT, 'h']),  # Replace (Cmd + Shift + H)
        # 4th row ----------
        (0x000000, 'Comm', [Keycode.COMMAND, Keycode.FORWARD_SLASH]),  # Toggle line comment (Cmd + /)
        (0x000000, 'Fold', [Keycode.COMMAND, Keycode.OPTION, Keycode.LEFT_ARROW]),  # Fold all (Cmd + Option + Left)
        (0x000000, 'Unfld', [Keycode.COMMAND, Keycode.OPTION, Keycode.RIGHT_ARROW]),  # Unfold all (Cmd + Option + Right)
        # Encoder button ---
        (0x000000, 'Save', [Keycode.COMMAND, 's'])   # Save (Cmd + S)
    ]
}