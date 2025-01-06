import os
import shutil
import sys

path = r"C:/Users/idfk"
charas = ["starting file names here"]
prefixes = ["differentiating text after charas"]
prefixesnew = ["8","7","6","5","4","3","2","1"]

count = len(prefixes)
if count != len(prefixesnew):
    sys.exit("you done fucked up")

for selected in charas:
    # make dir
    os.chdir(path)
    if not os.path.exists(selected):
        os.makedirs(selected)
    
    # move to dir
    for file_name in os.listdir (path):
        if file_name.startswith(selected + " "): 
            shutil.move(file_name,selected + "/" + file_name)

    # edit inside dir        
    os.chdir(path + "/" + selected)

    # first operation
    for i in range(count):
        target = selected + " " + prefixes[i]
        for file_name in os.listdir (path + "/" + selected):
            # replace prefixes
            if file_name.startswith(target):
                old_name = file_name
                new_name = file_name.replace (target, prefixesnew[i] + " ")
                os.rename (old_name, new_name)
            # fix extra spaces
            if "  " in file_name :
                old_name = file_name
                new_name = file_name.replace ("  ", " ")
                os.rename (old_name, new_name)

    # second operation
    names = os.listdir (path + "/" + selected)
    firsts = [x[0] for x in names]
    firsts.sort(reverse = True)
    amount = int(firsts[0])
    numold = list(range(1,amount+1))
    numtemp = list(range(-amount,0))
    numnew = list(reversed(numold))
    # reordering phase 1
    for i in range(amount):
        for file_name in os.listdir (path + "/" + selected):
            target = str(numold[i])
            temp = str(numtemp[i])
            if file_name.startswith(target):
                old_name = file_name
                new_name = file_name.replace (target + " ", temp + " ")
                os.rename (old_name, new_name)
    # reordering phase 2
    for i in range(amount):
        for file_name in os.listdir (path + "/" + selected):
            target = str(numtemp[i])
            new = str(numnew[i])
            if file_name.startswith(target):
                old_name = file_name
                new_name = file_name.replace (target, new)
                os.rename (old_name, new_name)
    # rename file end first phase
    for i in range(amount+1):
        version = 1
        for file_name in os.listdir (path + "/" + selected):
            target = str(i)
            if file_name.startswith(target):
                old_name = file_name
                new_name = target + " " + str(version) + "edit.png"
                version = version + 1
                os.rename (old_name, new_name)
    # rename file end second phase
    for i in range(amount+1):
        version = 1
        for file_name in os.listdir (path + "/" + selected):
            target = str(i)
            if file_name.startswith(target):
                old_name = file_name
                new_name = target + " " + str(version) + ".png"
                version = version + 1
                os.rename (old_name, new_name)