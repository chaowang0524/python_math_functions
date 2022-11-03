import datetime

current_datetime = datetime.datetime.now()
print(type(current_datetime), current_datetime)  # the result is in time format

# convert time format into str
str_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(type(str_time), str_time)  # the result is in string format


# get the current year and month
print(current_datetime.year, current_datetime.month)
# the result is an integer
print(type(current_datetime.month), current_datetime.month)
