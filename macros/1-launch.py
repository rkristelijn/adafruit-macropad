from adafruit_hid.keycode import Keycode

# For launching applications with shortcuts on macOS, first configure the shortcut in Shortcuts application:
#
# Open Shortcuts application.
# Click on the + button.
# All Shortcuts
# Search for Open app action and drag & drop it to the canvas
# In created action field click on App and search for an application you want to launch e.g. iTerm
# Created action field
# Click on Info icon (1), then on Add Keyboard Shortcut (2) and press your shortcut keys.
# Add keyboard shortcut e.g. Control + Option + Command + I
# That's it - shortcut is saved automatically
#
# @see https://apple.stackexchange.com/a/471760/595528 for more information

app = {         
    'name' : '1: Adafruit Launchpad',
    'macros' : [
        # 1st row ----------
        (0x000000, 'iTerm', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.I]),  # Control + Option + Command + I
        (0x000000, 'Chrome', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.C]),  # Control + Option + Command + C
        (0x000000, 'VSC', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.V]),  # Control + Option + Command + V
        # 2nd row ----------
        (0x000000, 'Teams', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.T]),
        (0x000000, 'ChatGPT', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.G]),
        (0x000000, 'Finder', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.F]),
        # 3rd row ----------
        (0x000000, '<<', [Keycode.COMMAND, Keycode.LEFT_BRACKET]),  # Swipe Left
        (0x000000, '>>', [Keycode.COMMAND, Keycode.RIGHT_BRACKET]), # Swipe Right
        (0x000000, '^^', [Keycode.CONTROL, Keycode.UP_ARROW]),
        # 4th row ----------
        (0x000000, 'Search', [Keycode.COMMAND, Keycode.SPACE]),
        (0x000000, 'Boss', [Keycode.F11]),
        (0x000000, 'Control', [Keycode.CONTROL, Keycode.UP_ARROW]),      # Mission Control
        
        # Encoder button ---
        (0x000000, 'Quit', [Keycode.COMMAND, Keycode.Q]) 
    ]
}

print("Launchpad app loaded")  # Debug print