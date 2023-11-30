import os
import shutil

source = "C:/Users/lscub/OneDrive/Documents/102/102.py"
dest = "C:/Users/lscub/OneDrive/Downloads/102/102.py"

list_files = os.listdir(source)
print(list_files)
for file_name in list_files:
    name,ext = os.path.splitext(file_name)
    #print(name)
    #print(ext)
    if ext == "":
        continue
    if ext in ['.png','.jpg'] :
        path1 = source + "/" + file_name
        path2 = dest + "/" + "result"
        path3 = path2 + "/" + file_name
        if os.path.exists (path2):
            print("moving" + file_name)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving" + file_name)
            shutil.move(path1,path3)

