from datetime import datetime

now = datetime.now() 

current_time = now.strftime("%H+:%M:%S")
print("The GMT time right now is", current_time)
