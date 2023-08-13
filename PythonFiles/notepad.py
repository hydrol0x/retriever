import time
import pyautogui
import subprocess

def open_notepad_and_type(text):
    # Open Notepad
    subprocess.Popen('notepad.exe')

    # Wait for Notepad to open (adjust this delay based on your system)
    time.sleep(1)

    # Type the given text using PyAutoGUI
    pyautogui.write(text)

