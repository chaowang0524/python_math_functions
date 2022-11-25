import re
import pandas as pd

with open("Assets/TGG.txt") as f:
    content = f.read()

# cannot split punctuations
# print(content.split())

# split with punctuations
words = re.split(r'[\s.()-?]+', content)

print(pd.Series(words).value_counts()[:20])
