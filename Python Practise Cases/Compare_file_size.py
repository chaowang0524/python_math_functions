"""Sum file sizes under one directory"""
import os
# print(os.path.getsize("TGG.txt"))

sum_size = 0  # count the sum of the file sizes
for file in os.listdir("."):  # os.listdir(".") is the current directory
    if os.path.isfile(file):  # only iterate file rather other directories
        sum_size += os.path.getsize(file)  # get one file size
sum_size = sum_size / 1000  # convert from bytes to kb
print(sum_size)
