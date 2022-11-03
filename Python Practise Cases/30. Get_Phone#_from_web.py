import re

dir = "Assets/phone#.txt"
all_numbers = []
with open(dir, "r") as f:
    # for line in f:
    #     line = line[:-1]
    #     result = re.findall(r'[1][3-9]\d{9}', line)
    #     all_numbers.append(result)
    # or read everything in one line `.read()`
    content = f.read()
    result = re.findall(r'[1][3-9]\d{9}', content)

print(result)
