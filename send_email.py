import time
import pyautogui
from pywinauto import Application

def open_mail_app_with_start_menu(recipient, subject, body):
    # Simulate key presses to open the Start menu
    pyautogui.press('win')

    # Wait for the Start menu to open (adjust the delay as needed)
    time.sleep(2)

    # Type "mail" to search for the Mail app
    pyautogui.write("mail", interval=0.1)
    time.sleep(1)

    # Open the Mail app from the search results
    pyautogui.press('enter')
    time.sleep(5)

    # Use pywinauto to find the Mail app window with title "Inbox -"
    app = Application(backend='uia').connect(title_re='Inbox -.*', timeout=10)
    mail_app_window = app.window(title_re='Inbox -.*')

    # Find the "New mail" button inside the "Inbox -" window and click it
    new_mail_button = mail_app_window.child_window(title="New mail", control_type="Button")
    if new_mail_button.exists():
        new_mail_button.click()

        # Wait for the new email window to open (adjust the delay as needed)
        time.sleep(5)
        # Type the recipient email(s) using pyautogui
        pyautogui.typewrite(recipient)

        # Press Tab three times using pyautogui
        pyautogui.press('tab', presses=3)

        # Type the subject line using pyautogui
        pyautogui.typewrite("Subject line")

        # Press Tab using pyautogui
        pyautogui.press('tab')

        # Type the body using pyautogui
        pyautogui.typewrite("This is the email body.")

        # Emulate Ctrl+Enter using pyautogui
        pyautogui.hotkey('ctrl', 'enter')

if __name__ == "__main__":
    # Call the functions to perform the actions
    recipient="dylaniscool1050@gmail.com"
    subject="Test Email"
    body="body of the email"
    open_mail_app_with_start_menu(recipient, subject, body)
