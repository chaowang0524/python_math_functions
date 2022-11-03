import datetime
# read the file
# put the data into a dictionary with date as key and sale as value


date_sale = {}

dir = "Assets/sales.txt"
with open(dir) as f:
    for line in f:
        line = line[:-1]
        date, sale = line.split("\t")
        date_sale[date] = sale
# remove the title or use python switch `first_line = False`
date_sale.pop('Date')
# print(date_sale)

# find the date that is X days before the selected date


def find_date(selected_date, x):
    selected_datetime = datetime.datetime.strptime(selected_date, "%Y/%m/%d")
    date_difference = datetime.timedelta(days=x)
    compared_date = selected_datetime - date_difference
    compared_date = compared_date.strftime('%Y/%m/%d')
    return compared_date


# find the sale_difference between the selected date and the selected days before
# use seven days as an example
for date, sale in date_sale.items():
    date_week_before = find_date(date, 7)
    sale_week_before = date_sale.get(date_week_before, 0)
    if sale_week_before == 0:
        print(date, sale, 0)
    else:
        sale_difference = int(date_sale[date]) - int(sale_week_before)
        print(sale_difference)
