""" Calculate the date A that is x days before date b"""


import datetime


def get_date(date_b: datetime.date, x: int) -> str:
    """Calculate the data a that is x days before date b

    Args:
        date_b (datetime.date): the late date
        x (int): the difference

    Returns:
        str: the old date, the date x days before the late date
    """

    date_b = datetime.datetime.strptime(
        date_b, "%Y-%m-%d")  # convert the date_a to string
    date_difference = datetime.timedelta(days=x)
    print(type(date_difference))
    date_a = date_b - date_difference
    print(type(date_a))
    date_a = date_a.strftime("%Y-%m-%d")

    return date_a


print(get_date("1991-05-24", 365))
