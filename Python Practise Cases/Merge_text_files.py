import os
data_dir = "/Users/chaowang/Documents/Python/Python Practise/100 Practise Cases/texts"

content = []
# scan each file's path under the directory
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"  # the correct path
    if os.path.isfile(file_path) and file.endswith(".txt"):

        # merge two files
        with open(file_path) as f:
            content.append(f.read())
content = "\n".join(content)  # separate the file with "\n"


# write to a new file
with open("Merged.txt", "a") as output_file:
    print(content, file=output_file, sep="\n")
