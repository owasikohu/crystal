#!/usr/bin/env python3

from Xlib import X, display, Xatom
import sys

def set_opacity(win_id, opacity):
    """
    win_id: ウィンドウID (16進 or 10進)
    opacity: 不透明度 0.0～1.0
    """

    # Xlib の Display を開く
    d = display.Display()
    win = d.create_resource_object('window', win_id)

    # 不透明度を 32bit の整数値に変換
    # 0xffffffff = 完全不透明
    value = int(opacity * 0xffffffff)

    atom = d.intern_atom('_NET_WM_WINDOW_OPACITY')

    # プロパティを変更
    win.change_property(atom, Xatom.CARDINAL, 32, [value])

    d.sync()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("使い方: python change_opacity.py <window id> <opacity 0.0 - 1.0>")
        sys.exit(1)

    win_id_str = sys.argv[1]
    if win_id_str.startswith("0x") or win_id_str.startswith("0X"):
        win_id = int(win_id_str, 16)
    else:
        win_id = int(win_id_str)

    opacity = float(sys.argv[2])

    set_opacity(win_id, opacity)
    print(f"ウィンドウ {hex(win_id)} の透明度を {opacity*100:.1f}% に設定しました。")

