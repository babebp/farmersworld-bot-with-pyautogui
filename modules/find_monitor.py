import pyautogui

class finding_monitor:
    def find_monitor():
        monitor = pyautogui.getWindowsWithTitle("Farmer")
        monitor_leng = len(monitor)
        return monitor, monitor_leng