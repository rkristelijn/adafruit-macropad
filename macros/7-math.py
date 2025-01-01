from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : '7: Math Symbols',  # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Pi', [Keycode.OPTION, Keycode.P]),  # π (Option + P)
        (0x000000, 'Sqrt', [Keycode.OPTION, Keycode.V]),  # √ (Option + V)
        (0x000000, 'Sum', [Keycode.OPTION, Keycode.W]),  # ∑ (Option + W)
        # 2nd row ----------
        (0x000000, 'Delta', [Keycode.OPTION, Keycode.J]),  # ∆ (Option + J)
        (0x000000, 'Theta', [Keycode.OPTION, Keycode.SHIFT, Keycode.J]),  # θ (Option + Shift + J)
        (0x000000, 'Integr', [Keycode.OPTION, Keycode.B]),  # ∫ (Option + B)
        # 3rd row ----------
        (0x000000, 'Infinity', [Keycode.OPTION, Keycode.FIVE]),  # ∞ (Option + 5)
        (0x000000, 'Degree', [Keycode.OPTION, Keycode.K]),  # ° (Option + K)
        (0x000000, '+/-', [Keycode.OPTION, Keycode.SHIFT, Keycode.EQUALS]),  # ± (Option + Shift + =)
        # 4th row ----------
        (0x000000, '<=', [Keycode.OPTION, Keycode.COMMA]),  # ≤ (Option + ,)
        (0x000000, '>=', [Keycode.OPTION, Keycode.PERIOD]),  # ≥ (Option + .)
        (0x000000, '!=', [Keycode.OPTION, Keycode.EQUALS]),  # ≠ (Option + =)
        # Encoder button ---
        (0x000000, '', [])   # Empty encoder button
    ]
}