import os

search_dir = "/Users/chaowang/Downloads"

# `search_dir` will return root, dirs and files
result_files = []
for root, dirs, files in os.walk(search_dir):
    for file in files:
        file_path = f"{root}/{file}"  # The correct path of the file
        result_files.append((file_path, os.path.getsize(file_path)/1000))
print(sorted(result_files, key=lambda x: x[1], reverse=True)[:10])
