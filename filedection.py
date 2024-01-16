#You have to wait the program finish to see it works
import os
running = True
while running:
    method = input("Find/Read/Write/Copy/Move/Delete :").lower()
    if method == "find":
        path = input("Enter a location you want to find:")
        if os.path.exists(path):
            print("That location exists")
            if os.path.isfile(path):
                print("It is a file")
            elif os.path.isdir(path):
                print("It is a folder")
        else:
            print("That location doesn't exists")
    elif method == "read":
        try:
            source = input("Enter file name:")  # remove " "
            with open(source) as file:
                print(file.read())
        except FileNotFoundError:
            print("That file was not found")
        except Exception:
            print("Error occured!Please check again.")
    elif method == "write": #write file will be written in the same project folder where you place this file
        text = input("Write:\n")
        style = input("Overwrite(O) or Append(A):").upper()
        if style == "O":
            with open("write", 'w') as file:
                file.write(text)
        elif style == "A":
            with open("write", 'a') as file:
                file.write(text)
        else:
            print("Something went wrong....")
    elif method =="copy":
        origin = input("Enter a file to copy:")
        copy = input("Save this file name as :")
        import shutil
        try:
            if os.path.exists(origin):
                if os.path.isfile(origin):
                    shutil.copyfile(origin, copy)
                    print("File was copied.")
                elif os.path.isdir(origin):
                    print("Can't copy a folder")
            else:
                print("Can't find any file to copy")
        except OSError:
            print("Something went wrong!!")
    elif method == "move":
        soc = input("Enter a file to move:")
        des = input("Move this file to   :")
        try:
            if os.path.exists(des):
                print("There is already a file there")
            else:
                os.replace(soc,des)
                print(soc+" was moved successfully.")
        except FileNotFoundError:
            print(soc+" was not found")
    elif method == "delete":
        import shutil
        delete = input("Enter a file to delete:")
        try:
            if os.path.isdir(delete):
                shutil.rmtree(delete)
            elif os.path.isfile(delete):
                os.remove(delete)
        except FileNotFoundError:
            print("There is no file.")
        except PermissionError:
            print("Permission denied")
        else:
            print(delete+" was deleted")
    else:
        print("Type again carefully!")
    if not input("Enter R to try again/Press any other key to quit:").upper()== "R":
        running=False
        print("See ya again...")
