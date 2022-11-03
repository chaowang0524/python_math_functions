import datetime

birthday = "1991-05-24"

# convert the birthday string into a datetime object
birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
# print(birthday_date)

# get the current date and time
now = datetime.datetime.now()

# calculate the difference between``
difference = (now - birthday_date).days

print(difference)
