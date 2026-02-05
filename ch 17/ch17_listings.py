# 17.1 creating a date
import datetime

ada_bday = datetime.date(1815, 12, 10)
print(ada_bday)

# 17.2 prompting for a date
import datetime

year = input("Please enter a year from 1900 to 2100: ")
while True:
    if int(year) >= 1900 and int(year) <= 2100:
        break
    else:
        year = input("Please enter a VALID year from 1900 to 2100: ")

month = input("Please enter a month from 1 to 12: ")
while True:
    if int(month) >= 1 and int(month) <=12:
        break
    else:
        month = input("Please enter a VALID month from 1 to 12: ")
        
day = input("Please enter a day from 1 to 31: ")
while True:
    if int(day) >= 1 and int(day) <= 31:
        break
    else:
        day = input("Please enter a VALID day from 1 to 31: ")

user_date = datetime.date(int(year),int(month),int(day))
print(user_date)

# 17.3 Creating a time
import datetime
appointment = datetime.time(10,30,00)
print("Appointment time: " + str(appointment))

# 17.4 Creating a datetime
import datetime
appointment = datetime.datetime(2022, 12, 10, 10, 30, 00)
print("Appointment time: " + str(appointment))

# datetime(year, month, day, hour, minutes, second)

# 17.5 What time is it now?
import datetime

time_now = datetime.datetime.now()
print(time_now)

# 17.6 Splitting a date
d = "2022-07-23 11:26:26.050403"
(d,t) = d.split()
(year,month,day) = d.split("-")
print(year)
print(month)
print(day)

# 17.7 Splitting the time
d = "2022-07-23 11:26:26.050403"
(d,t) = d.split()
(hour, minute, second) = t.split(":")
print(hour)
print(minute)
print(second)

# 17.8 Splitting the date and time
import datetime
d = datetime.datetime.now()
d = str(d)

(d,t) = d.split()
(year,month,day) = d.split("-")
(hour, minute, second) = t.split(":")
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

# 17.9 Extracting with datetime attributes
import datetime

time_now = datetime.datetime.now()

print(time_now)
print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)
print(time_now.microsecond)
print(time_now.tzinfo)

# 17.10 Creating a custom date with need parameters
import datetime

t1 = datetime.date(year = 2013, day = 4, month = 12)
t2 = datetime.date(year = 2013, month = 12, day = 4)
t3 = datetime.date(day = 4, year = 2013, month = 12)

# 17.11 Comparing dates
import datetime
d1 = datetime.datetime(year = 2013, month = 12, day = 4)
d2 = datetime.datetime(year = 2014, month = 3, day = 12)

print(d1 > d2)
print(d1 < d2)
print(d1 == d2)

# 17.12 Past, future or present
import datetime
year = int(input("Please enter a year: " ))
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: " ))

d1  = datetime.date(year, month,day)
today = datetime.datetime.today().date()

if d1 > today:
    print("That date is in the future.")
elif d1 < today:
    print("The date is in the past.")
elif d1 == today:
    print("The date is today!")

# 17.13 Working with the UTC dates
import datetime
time_utc_now = datetime.datetime.utcnow()