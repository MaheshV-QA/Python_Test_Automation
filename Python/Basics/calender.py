import calendar

# 1. Print a full year's calendar
print("Full calendar for 2025:")
print(calendar.calendar(2025))

# 2. Get the first weekday of the month and number of days in the month
first_weekday, total_days = calendar.monthrange(2025, 4)
print(f"April 2025 starts on weekday {first_weekday} (0=Monday) and has {total_days} days.")

# 3. Get the weekday of a specific date
weekday = calendar.weekday(2025, 4, 15)  # year, month, day
print(f"April 15, 2025 falls on weekday: {weekday} (0=Monday)")

# 4. Set the first day of the week (default is Monday, 0)
calendar.setfirstweekday(calendar.SUNDAY)
print("April 2025 with Sunday as the first day of the week:")
print(calendar.month(2025, 4))

# 5. Generate an iterator for all weeks in a month
weeks = calendar.monthcalendar(2025, 4)
print("Weeks in April 2025:")
for week in weeks:
    print(week)  # each list shows days in the week (0 for days outside the month)

# 6. List leap years in a range
print("Leap years from 2000 to 2030:")
for year in range(2000, 2031):
    if calendar.isleap(year):
        print(year, end=" ")
print()  # clean line break
