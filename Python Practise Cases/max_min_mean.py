

def compute_score():
    """read file, get the data and compute_score"""

    scores = []
    with open("input.txt") as f:
        for line in f:
            line = line[:-1]
            fields = line.split(",")  # `fields` is a list
            # convert string to integer before append to list
            scores.append(int(fields[2]))

    max_score = max(scores)
    min_score = min(scores)
    mean = sum(scores) / len(scores)
    return max_score, min_score, mean


print(compute_score())
