import pywhatkit as kit
import datetime

# Schedule the message for 2 minutes from the current time
now = datetime.datetime.now()
target_number = "+940742774336" # Replace with your test number

print(f"Scheduling message for {now.hour}:{now.minute + 2}...")
kit.sendwhatmsg(target_number, "I LOVE YOU SO MUCH PRINCESS", now.hour, now.minute + 2)