# MS Teams Hotkeys (MacOS)
# source: https://github.com/armccoy/macropad-rp2040-hotkeys/blob/main/macros/teams.py

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'A: MS Teams        ', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Audio', [Keycode.COMMAND, Keycode.SHIFT, Keycode.M]),
        (0x000000, 'Chat', [Keycode.COMMAND, 2]),
        (0x000000, 'Video', [Keycode.COMMAND, Keycode.SHIFT, Keycode.O]),
        # 2nd row ----------
        (0x000000, 'Share', [Keycode.COMMAND, Keycode.SHIFT, Keycode.E]),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (0x000000, 'Leave', [Keycode.COMMAND, Keycode.SHIFT, Keycode.H]),
        # 3rd row ----------
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        # 4th row ----------
        (0x000000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x000000, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000000, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
} 