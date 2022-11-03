import datetime
unix_time = 1620747647

# convert to datetime format
_datetime = datetime.datetime.fromtimestamp(unix_time)

# convert the object to string

datetime_str = _datetime.strftime("%Y-%m-%d %H:%M:%S")

print(type(datetime_str), datetime_str)
