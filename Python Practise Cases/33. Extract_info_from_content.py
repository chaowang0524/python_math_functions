import re

content = """
Sean went to shopping:
He bought 1 cucumber with $5
He bought 2 grapes with $10
He bought 3 cabbages with $8.5
"""


for line in content.split('\n'):
    pattern = r'(\d)\s(.+)\swith\s(.+)'
    result = re.search(pattern, line)
    if result:
        print(result.groups())

