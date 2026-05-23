# Working with `datetime` and `date` modules

from datetime import datetime
from datetime import date

# Get current time in HH:MM:SS format
time_now = datetime.now().strftime('%H:%M:%S')
print("Current Time:", time_now)

# Get today's date in YYYY-MM-DD format
today_date = date.today()
print("Today's Date:", today_date)
