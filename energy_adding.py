from pickletools import pybytes
import pyautogui
import time

class energy:
    def add_energy():
        print('---------Start Energy Adding---------')
        pyautogui.click(1715, 140)
        time.sleep(2)
        pyautogui.click(995, 523)
        pyautogui.write('999')
        pyautogui.click(930, 617)
        time.sleep(8)
        pyautogui.click(338, 522)
        print('---------Energy Adding Success---------')