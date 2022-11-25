import re


content = """
白日依19989881888山尽, 黄河入45645546468798978海流。
欲穷12345千里目, 更上15619292345一层楼。
"""

pattern = r'(1[3-9])\d{9}'  # in line with the phone number format
# use r"\1" to isolate the first group (the two numbers)
result = re.sub(pattern, r"\1******", content)
print(result)
