import pyautogui
import time

user_text="Get from CMD line args"

# Press the Windows key.
pyautogui.press('win')

# Wait for the start menu to open.
time.sleep(1)

# Type "Notepad" and press enter.
pyautogui.write('Notepad')
pyautogui.press('enter')

time.sleep(2)
pyautogui.write(user_text)