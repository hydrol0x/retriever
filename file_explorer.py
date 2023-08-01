import time
import pyautogui
from pywinauto import Application

def get_file(file_name):
    # Simulate key presses to open the Start menu
    pyautogui.press('win')

    # Wait for the Start menu to open (adjust the delay as needed)
    time.sleep(2)

    # Type "mail" to search for the Mail app
    pyautogui.write(f"file: {file_name}", interval=0.1)
    time.sleep(1)

    # Open the Mail app from the search results
    pyautogui.press('enter')
    time.sleep(5)
