"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

# https://www.geeksforgeeks.org/python-calendar-module/
#
import sys
import calendar
from datetime import date

# just shows cal for given month and yar


# https://www.w3resource.com/python/module/calendar/prmonth.php
"""
x = input("add month and year here: ")
calendar.prmonth(int(x[0]), int(x[1]))
"""

# https://stackoverflow.com/questions/26226489/how-do-you-get-python-to-detect-for-no-input
"""
x = input("add month and year here: ")
print(len(x))

for x in range(0, 1):
    t = calendar.prmonth(int(x[0]), int(x[1]))
    print(t)
"""

x = input("Enter comma seperated values for year, then month: ").split(',')
print(x)
# read ya errors kid!! the 2nd arg for calendar.prmonth is month not year
# so its only got 2 places/integers you can put~ 1st arg = year, 2nd = month
today = date.today()

if int(x[0]) and int(x[0]) <= 12:
    print(int(x[0]))
    d5 = int(today.strftime("%Y"))
    p = int(x[0][:2])
    print("p", p)
    print(calendar.prmonth(d5, p))
elif len(x) == 2:
    m = int(x[0])
    r = int(x[1])
    print(calendar.prmonth(m, r))
elif int(x[0]) == 0 or int(x[0]) > 12:
    print("month argument must be between range 1-12")
else:
  # datetime tof
    d4 = int(today.strftime("%m"))
    d5 = int(today.strftime("%Y"))
    print(calendar.prmonth(d5, d4))
