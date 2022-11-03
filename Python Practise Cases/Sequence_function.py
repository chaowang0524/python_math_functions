# class Sequence():
import math


def find_median(sequence):
    sequence = sorted(sequence)
    if len(sequence) == 1:
        return sequence[0]
    elif len(sequence) % 2 == 0:
        result = (sequence[len(sequence)//2] +
                  sequence[(len(sequence)//2)-1]) / 2.0
    else:
        result = (sequence[len(sequence)//2])
    return result


def find_iqr(sequence):  # calculate the interquartile range
    if len(sequence) % 2 == 0:
        q_1 = find_median(sequence[:(len(sequence) // 2)])
        q_3 = find_median(sequence[-(len(sequence) // 2):])
    else:
        q_1 = find_median(sequence[:(len(sequence) // 2)])
        q_3 = find_median(sequence[-(len(sequence) // 2):])
    result = q_3 - q_1
    return result


def find_stdev(sequence):  # calculate the population standard deviation and variance
    miu = sum(sequence)/len(sequence)
    dev = 0
    for i in sequence:
        dev += (i - miu) ** 2
    result = math.sqrt(dev / len(sequence))
    # variance = dev / len(sequence)
    return result


def find_sample_variance(sequence):
    miu = sum(sequence)/len(sequence)
    dev = 0
    for i in sequence:
        dev += (i - miu) ** 2
    result = dev / (len(sequence) - 1)
    # sample_stdev = math.sqrt(result) # calculate the sample standard deviation
    return result

def find_mad(sequence):
    miu = sum(sequence) / len(sequence)
    result = 0
    for i in sequence:
        result += abs(i - miu)
    result = result / len(sequence)
    return result