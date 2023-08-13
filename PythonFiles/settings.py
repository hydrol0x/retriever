import time
import pyautogui
from pywinauto import Application

def open_settings(setting_name):
    # Simulate key presses to open the Start menu
    pyautogui.press('win')

    # Wait for the Start menu to open (adjust the delay as needed)
    time.sleep(2)

    # Type "mail" to search for the Mail app
    pyautogui.write("settings", interval=0.1)
    time.sleep(1)

    # Open the Mail app from the search results
    pyautogui.press('enter')
    time.sleep(5)

    # Use pywinauto to find the Mail app window with title "Inbox -"
    app = Application(backend='uia').connect(title_re='Settings', timeout=10)
    mail_app_window = app.window(title_re='Settings')

    # Find the "New mail" button inside the "Inbox -" window and click it
    pyautogui.typewrite(setting_name)

    # Press Tab three times using pyautogui
    pyautogui.press('enter')
if __name__ == "__main__":
    open_settings("sound")