import os

path = r"C:/Users/whateverthefuck"
os.chdir(path)

for file_name in os.listdir (path):
    if "mav" in file_name :
        old_name = file_name
        print(old_name)
        new_name = file_name.replace ("idk vol 1", "idk vol 2")
        print(new_name)
        os.rename (old_name, new_name)