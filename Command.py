from pynput.keyboard import Key, Controller
from typing import List


class KeyCommand:

    def __init__(self):
        self.keyboard = Controller()

        self.keyBindings = {
           "alt":Key.alt,
           "f12":Key.f12
        }

        self.dictionaryKeys = list(self.keyBindings.keys())

    def keyPress(self,keySet:List[str]):

        for key in keySet:
            if key in self.dictionaryKeys:
                self.keyboard.tap(self.keyBindings[key])
            else:
                self.keyboard.tap(key)






