from find_monitor import finding_monitor
from water_auto import water
from line_notify import line
from energy_adding import energy
import pyautogui

monitor_loc ,monitor_leng = finding_monitor.find_monitor()

while True:
        ## Open Monitor ##
        monitor_loc[1].minimize()
        monitor_loc[0].minimize()
        monitor_loc[0].maximize()
        water.watering()
        energy.add_energy()
        pyautogui.screenshot('main.png')
        line.line_pic('ของแม่', 'main.png')

        monitor_loc[1].minimize()
        monitor_loc[0].minimize()
        monitor_loc[1].maximize()
        water.watering()
        energy.add_energy()
        pyautogui.screenshot('main.png')
        line.line_pic('ของพ่อ', 'main.png')

    