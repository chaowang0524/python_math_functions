import jieba.posseg as posseg
import pandas as pd
# content = "李明喜欢韩梅梅，他俩早恋了"

# for word, flag in posseg.cut(content):
#     if flag == "nr":
#         print(word, flag)

names = []
with open("Assets/《鹿鼎记》.txt") as f:
    content = f.read()
    for word, flag in posseg.cut(content):
        if flag == "nr":
            names.append(word)

# use pandas to count the number of names
# first 20 names appeared most times
print(pd.Series(names).value_counts()[:20])
