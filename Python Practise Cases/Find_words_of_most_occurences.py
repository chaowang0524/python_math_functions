def find_most_occurance() -> dict:
    # use dictionary to count the word and its occurences
    word_count = {}
    with open("TGG.txt") as f:
        for line in f:  # read by lines
            line = line[:-1]  # remove the \n
            words = line.split(" ")  # seperate the words in the sentences
            for word in words:  # iterate over each sentence
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    return word_count


# when sorting a dictionary using sorted(),
# retriev the key and value pairs using item()
# then sorted with lambda
# reverse = True to find the most used word
result = sorted(find_most_occurance().items(),
                key=lambda x: x[1], reverse=True)[:10]  # only show first 10 pairs
print(result)
