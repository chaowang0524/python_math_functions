import re

content = """
白日依2021/05/26山尽,黄河入2021.05.27海流。
飲穷05-28-2020千里目,更上5/29/2020一层楼。
"""
# target format: 2021-05-28

pattern_1 = r'(\d{4})/(\d{2})/(\d{2})'
pattern_2 = r'(\d{4})\.(\d{2})\.(\d{2})'
pattern_3 = r'(\d{2})-(\d{2})-(\d{4})'
pattern_4 = r'(\d{1})/(\d{2})/(\d{4})'
# use groups to replace
content = re.sub(pattern_1, r'\1-\2-\3', content)
content = re.sub(pattern_2, r'\1-\2-\3', content)
content = re.sub(pattern_3, r'\3-\1-\2', content)
content = re.sub(pattern_4, r'\3-0\1-\2', content)
print(content)

