from datetime import datetime

time_12hr = "02:30 PM"
time_24hr = datetime.strptime(time_12hr, "%I:%M %p").strftime("%H:%M")
print("24-hour format:", time_24hr)