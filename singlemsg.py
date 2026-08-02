import pywhatkit as kit
import time
import pyautogui

target_number = "+940742774336"

message = "Day 1: Automated message"
print("Opening whatsapp web")

kit.sendwhatmsg_instantly(target_number, message, wait_time=15)

time.sleep(2)
pyautogui.press('enter')

print("message sent successfully")



