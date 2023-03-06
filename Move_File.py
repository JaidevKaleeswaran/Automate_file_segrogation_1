import os
import shutil

from_dir = "/Users/jaidevkaleeswaran/Downloads"
to_dir = "/Users/jaidevkaleeswaran/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)