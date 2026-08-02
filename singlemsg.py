import pywhatkit as kit
import datetime

now = datetime.datetime.now()
target_number = "+940702233100"

print(f"Scheduling message for {now.hour}:{now.minute + 2}.....")
kit.sendwhatmsg(target_number, "Day 1: Automated message", now.hour, now.minute +2)
