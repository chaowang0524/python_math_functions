"""Calculate all the dates between the given interval """
import datetime


# add one day to the begin_date, print out the date till the given end_date
def date_between_interval(begin_date: str, end_date: str) -> list:
    result = []
    while begin_date <= end_date:  # python can compare between two strings
        result.append(begin_date)  # put the begin date to the list
        # convert begin date string format to datetime format
        begin_datetime = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        # add one day to the begin date
        one_day = datetime.timedelta(days=1)
        begin_datetime += one_day
        # convert back to string format
        begin_date = begin_datetime.strftime(
            "%Y-%m-%d")  # convert back to string format

    return result


print(date_between_interval("1991-05-24", "1991-06-08"))
print(("1991-05-24" < "1991-06-08"))
