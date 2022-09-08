import time, math

# more text things (1 = yes, 0 = no)
m = 0

# zone (1 = EST, 0 = UTC)
e = 1

time = time.time()

# account for year 2000 not having a leap day
time = time + 86400

if e == 1:
  time = time - 14400

if m == 1:
  print("I can turn this number:")
  print(math.floor(time * 100))
  print("")
  print("Into this:")

year = math.floor(time / 31557600)
time = time - (year * 31557600)
year = year + 1970
day = math.floor(time / 86400)
time = time - (day * 86400)
hour = math.floor(time / 3600)
time = time - (hour * 3600)
minute = math.floor(time / 60)
time = time - (minute * 60)
time = time * 100
second = math.floor(time)


if len(str(minute)) == 1:
  min1 = minute
  minute = "0" + str(min1)

second = second / 100

monthNum = day

# check if leap year
if year % 4 == 0:
  if monthNum <= 31:
    month = "Janurary"
  elif monthNum <= 60:
    month = "Feburary"
    monthNum = monthNum - 31
  elif monthNum <= 91:
    month = "March"
    monthNum = monthNum - 60
  elif monthNum <= 121:
    month = "April"
    monthNum = monthNum - 91
  elif monthNum <= 152:
    month = "May"
    monthNum = monthNum - 121
  elif monthNum <= 182:
    month = "June"
    monthNum = monthNum - 152
  elif monthNum <= 213:
    month = "July"
    monthNum = monthNum - 182
  elif monthNum <= 244:
    month = "August"
    monthNum = monthNum - 213
  elif monthNum <= 274:
    month = "September"
    monthNum = monthNum - 244
  elif monthNum <= 305:
    month = "October"
    monthNum = monthNum - 274
  elif monthNum <= 335:
    month = "November"
    monthNum = monthNum - 305
  elif monthNum <= 366:
    month = "December"
    monthNum = monthNum - 335
  else:
    month = "INVALID NUMBER"
  
else:
  if monthNum <= 31:
    month = "Janurary"
  elif monthNum <= 59:
    month = "Feburary"
    monthNum = monthNum - 31
  elif monthNum <= 90:
    month = "March"
    monthNum = monthNum - 59
  elif monthNum <= 120:
    month = "April"
    monthNum = monthNum - 90
  elif monthNum <= 151:
    month = "May"
    monthNum = monthNum - 120
  elif monthNum <= 181:
    month = "June"
    monthNum = monthNum - 151
  elif monthNum <= 212:
    month = "July"
    monthNum = monthNum - 181
  elif monthNum <= 243:
    month = "August"
    monthNum = monthNum - 212
  elif monthNum <= 273:
    month = "September"
    monthNum = monthNum - 243
  elif monthNum <= 304:
    month = "October"
    monthNum = monthNum - 273
  elif monthNum <= 334:
    month = "November"
    monthNum = monthNum - 304
  elif monthNum <= 365:
    month = "December"
    monthNum = monthNum - 334
  else:
    month = "INVALID NUMBER"
if hour > 12:
  ap = "PM"
  hour -= 12
else:
  ap = "AM"

if m == 1:
  print(str(year) + " " + str(day) + " " + str(hour) + " " + str(minute) + " " + str(second))
  print("")
  print("Into this:")
if e == 0:
  print("Today is " + month + " " + str(monthNum) + ", " + str(year) + " at " + str(hour) + ":" + str(minute) + " " + ap + " and " + str(second) + " seconds. (UTC)")
else:
  print("Today is " + month + " " + str(monthNum) + ", " + str(year) + " at " + str(hour) + ":" + str(minute) + " " + ap + " and " + str(second) + " seconds. (EST)")
if m == 1:
  print("")
  print("All through the power of epoch and logic.")
  print("Kinda cool, right?")
