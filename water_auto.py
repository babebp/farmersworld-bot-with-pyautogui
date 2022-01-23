import pyautogui
import time
from line_notify import line

## Coordinate for each image ##
water_button = (1037, 665)
approve_button = (338, 522)
barley_img = [(642, 385), (650, 464), (645, 555), (649, 646), (647, 421), (647, 510), (648, 599), (648, 685)]

class water:
    def loop_water(start, stop):
        for i in range(4):
            ## Click each barley images ##
            pyautogui.click(barley_img[i])
            time.sleep(1)

            ## Click Water Button ##
            pyautogui.click(water_button)
            time.sleep(10)

            ## Click Approve Button ##
            pyautogui.click(180, 491)
            time.sleep(2)

            print(f'Barley {i + 1} Success')

    def watering():
        print('---------Start Watering---------')
        time.sleep(1)

        ## Start Water for 8 plots ##
        water.loop_water(0,3)
        
        ## Scroll down for last 4 barley images ##
        pyautogui.moveTo(652, 539)
        time.sleep(1)
        pyautogui.scroll(-10000)
        time.sleep(1)

        ## Water last 4 barley images ##
        water.loop_water(4,7)
        
        ## Scroll Up ready for next round ##
        pyautogui.moveTo(652, 539)
        pyautogui.scroll(10000)
        time.sleep(1)

