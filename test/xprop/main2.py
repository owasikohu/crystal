#!/usr/bin/env python3

from Xlib import X, display, Xatom

d = display.Display()

win_id = int(input("Window ID (10進 or 16進): "), 0)
win = d.create_resource_object('window', win_id)
atom = d.intern_atom('_NET_WM_WINDOW_OPACITY')

while True:
    try:
        val = input("opacity [0.0 - 1.0] > ")
        opacity = float(val)
        value = int(opacity * 0xffffffff)
        win.change_property(atom, Xatom.CARDINAL, 32, [value])
        d.sync()
        print(f"Set opacity to {opacity*100:.1f}%")
    except KeyboardInterrupt:
        print("\nBye!")
        break
    except Exception as e:
        print(f"Error: {e}")

