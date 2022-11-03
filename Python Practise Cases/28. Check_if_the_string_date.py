import re

date_1 = "2021-05-20"


def is_date(string: str) -> str:
    # result = re.findall(r'[0-9].+[0-9]', string)
    # result = re.match(r'[0-9].+[0-9]', string)
    result = re.findall(r'\d{4}-\d{2}-\d{2}', string)
    return result is not None


is_date(date_1)
