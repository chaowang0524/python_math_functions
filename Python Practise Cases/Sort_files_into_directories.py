import os
import shutil
dir = "/Users/chaowang/Downloads"
# use os.path.splitext to get the extension
for file in os.listdir(dir):
    # if os.path.isfile(file):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):  # if there is no such directory
        os.makedirs(f"{dir}/{ext}")  # create the directory
    # move the file to the correct directory
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)
