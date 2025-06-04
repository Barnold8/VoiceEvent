from pynput.keyboard import Key, Controller
from typing import List

"""
This file serves as the container in which actions are made. For example, the action of pressing a key, or moving the mouse, all of it is here.
"""

class KeyCommand:

    def __init__(self):
        self.keyboard = Controller()

        self.keyBindings = { # please tell me this is all of them
           "alt":Key.alt,
           "alt_gr":Key.alt_gr,
           "alt_l":Key.alt_l,
           "alt_r":Key.alt_r,
           "backspace":Key.backspace,
           "caps_lock":Key.caps_lock,
           "cmd":Key.cmd,
           "cmd_l":Key.cmd_l,
           "cmd_r":Key.cmd_r,
           "ctrl":Key.ctrl,
           "ctrl_l":Key.ctrl_l,
           "ctrl_r":Key.ctrl_r,
           "delete":Key.delete,
           "down":Key.down,
           "end":Key.end,
           "enter":Key.enter,
           "home":Key.home,
           "insert":Key.insert,
           "left":Key.left,
           "right":Key.right,
           "up":Key.up,
           "down":Key.down,
           "caps_lock":Key.caps_lock,
           "insert":Key.insert,
           "esc":Key.esc,
           "media_next":Key.media_next,
           "media_previous":Key.media_previous,
           "media_play_pause":Key.media_play_pause,
           "media_stop":Key.media_stop,
           "media_volume_down":Key.media_volume_down,
           "media_volume_up":Key.media_volume_up,
           "media_volume_mute":Key.media_volume_mute,
           "num_lock":Key.num_lock,
           "page_up":Key.page_up,
           "page_down":Key.page_down,
           "pause":Key.pause,
           "print_screen":Key.print_screen,
           "scroll_lock":Key.scroll_lock,
           "shift_r":Key.shift_r,
           "shift":Key.shift,
           "shift_l":Key.shift_l,
           "alt":Key.alt,
           "f1":Key.f1,
           "f2":Key.f2,
           "f3":Key.f3,
           "f4":Key.f4,
           "f5":Key.f5,
           "f6":Key.f6,
           "f7":Key.f7,
           "f8":Key.f8,
           "f9":Key.f9,
           "f10":Key.f10,
           "f11":Key.f11,
           "f12":Key.f12,
           "f13":Key.f13,
           "f14":Key.f14,
           "f15":Key.f15,
           "f16":Key.f16,
           "f17":Key.f17,
           "f18":Key.f18,
           "f19":Key.f19,
           "f20":Key.f20,
           "f21":Key.f21,
           "f22":Key.f22,
           "f23":Key.f23,
           "f24":Key.f24,
        }

        self.dictionaryKeys = list(self.keyBindings.keys())

    def keyPress(self,keySet:List[str]):

        for key in keySet:
            if key in self.dictionaryKeys:
                self.keyboard.tap(self.keyBindings[key])
            else:
                self.keyboard.tap(key)






