from find_monitor import finding_monitor
from water_auto import water
from line_notify import line
from energy_adding import energy
import pyautogui

monitor_loc ,monitor_leng = finding_monitor.find_monitor()

print(f'Farmersworld Detected : {monitor_leng}')

while True:
        for i in range(monitor_leng):
                ## Open Monitor ##
                monitor_loc[i].minimize()
                monitor_loc[i].maximize()
                water.watering()
                energy.add_energy()

                ## Screenshot for line notify ##
                pyautogui.screenshot('main.png')
                line.line_pic(f'Monitor : {i}', 'main.png')