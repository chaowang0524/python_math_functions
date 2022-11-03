# read file
import xdrlib


def read_file() -> list:
    result = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line[:-1]  # remove the \n in the end of the line
            result.append(line.split(","))

    return result


data = read_file()

# print(data)


# sort data according to grades


def sort_grades(x):
    # convert the string to integer when sorting
    d = sorted(x, key=lambda x: int(x[2]))
    return d


d = sort_grades(data)


print(d)


# write to file
def write_file(x):

    with open("output.txt", "w") as f:
        for i in x:
            f.write(",".join(i) + "\n")  # write file in lines (notice the \n)


write_file(d)
