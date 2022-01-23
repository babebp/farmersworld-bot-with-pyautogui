from pickletools import pybytes
import pyautogui
import time

## Coordinate for each image ##
plus_sign = (1715, 140)
input_field = (995, 523)
exchange_button = (930, 617)
approve_button = (338, 522)

class energy:
    def add_energy():
        print('---------Start Energy Adding---------')
        pyautogui.click(plus_sign)
        time.sleep(2)
        pyautogui.click(input_field)
        pyautogui.write('999')
        pyautogui.click(exchange_button)
        time.sleep(8)
        pyautogui.click(approve_button)
        time.sleep(2)
        print('---------Energy Adding Success---------')