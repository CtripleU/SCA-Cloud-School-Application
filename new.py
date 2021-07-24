from datetime import datetime
import pytz


WAT = pytz.timezone('Africa/Lagos')
now = datetime.now(WAT)

current_time = now.strftime("%H:%M:%S")
print("The time in Nigeria is", current_time)
