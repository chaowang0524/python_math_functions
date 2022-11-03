
# from Sequence_function import *

# a = "arstarstarst,arstarstarstatdtrsdrstd,xzvczxcvxcv"

# fields = a.split(",")  # convert into a list

# print(fields)


# print("3" < "2")

# a = [i *2 for i in a]
# print(a)

# def censor(text, word):
#     result = []
#     word_star_list = ["*" for w in word]
#     word_star = "".join(word_star_list)
#     print(word_star)
#     text_list = text.split(" ")
#     print(text_list)
#     for w in text_list:
#         if w != word:
#             result.append(w)
#         else:
#             result.append(word_star)
#     return " ".join(result)


# censor("hey hey hey", "hey")


# def count(sequence, item):
#   count_times = 0
#   for i in sequence:
#     if i == item:
#       count_times += 1
#       continue
#   return count_times

# count([1,2,1,1],1)

# def furify(x_list):
#   result = []
#   for i in x_list:
#     if i % 2 ==0:
#       result.append(i)
#   return result


# def product(numbers):
#   result = 1
#   for n in x:
#     result *= n
#   return result

# def median(sequence):
#     sequence = sorted(sequence)
#     print(sequence)
#     print(f'Length: {len(sequence)}')
#     # print(sequence)
#     if len(sequence) == 1:
#         return sequence[0]
#     elif len(sequence) % 2 == 0:
#         result = (sequence[len(sequence)//2] +
#                   (sequence[len(sequence)//2-1])) / 2.0
#     else:
#         result = (sequence[len(sequence)//2])
#     return result


# print(a[0:4])
# median(a)


# b = [1, 2, 3, 3, 4, 4, 4, 6]
# print(sum(b)/len(b))

a = [35, 39, 40, 40, 42, 44]

# print(f'Mean = {sum(a)/len(a)}')
# print(f'Median = {find_median(a)}')
# print(f'IQR = {find_iqr(a)}')
# print(f'Population variance = {find_stdev(a)**2}')
# print(f'Sample variance = {find_sample_variance(a)}')
# print(f'Standard deviation = {find_stdev(a)}')
# print(f'Sample standard deviation = {math.sqrt(find_sample_variance(a))}')
# print(f'MAD = {find_mad(a)}')


a = set(a)
print(a)