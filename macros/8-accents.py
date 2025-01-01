from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : '8: Dutch Accents',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
       # 1st row ----------
        (0x000000, '/e', [Keycode.OPTION, 'e', 'e']),  # é (Option + e, e)
        (0x000000, ':e', [Keycode.OPTION, 'u', 'e']),  # ë (Option + u, e)
        (0x000000, '\\e', [Keycode.OPTION, '`', 'e']),  # è (Option + `, e)
        # 2nd row ----------
        (0x000000, '/a', [Keycode.OPTION, 'e', 'a']),  # á (Option + e, a)
        (0x000000, ':a', [Keycode.OPTION, 'u', 'a']),  # ä (Option + u, a)
        (0x000000, '\\a', [Keycode.OPTION, '`', 'a']),  # à (Option + `, a)
        # 3rd row ----------
        (0x000000, '/o', [Keycode.OPTION, 'e', 'o']),  # ó (Option + e, o)
        (0x000000, ':o', [Keycode.OPTION, 'u', 'o']),  # ö (Option + u, o)
        (0x000000, '\\o', [Keycode.OPTION, '`', 'o']),  # ò (Option + `, o)
        # 4th row ----------
        (0x000000, '/u', [Keycode.OPTION, 'e', 'u']),  # ú (Option + e, u)
        (0x000000, ':u', [Keycode.OPTION, 'u', 'u']),  # ü (Option + u, u)
        (0x000000, '\\u', [Keycode.OPTION, '`', 'u']),  # ù (Option + `, u)
        # Encoder button ---
        (0x000000, '', [])   # Empty encoder button
    ]
}