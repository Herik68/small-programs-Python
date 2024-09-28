import os
import shutil

def find():
    path = input("Enter a location you want to find: ")
    if os.path.exists(path):
        print("That location exists")
        if os.path.isfile(path):
            print("It is a file")
        elif os.path.isdir(path):
            print("It is a folder")
    else:
        print("That location doesn't exist")

def read():
    source = input("Enter file name: ")
    try:
        with open(source) as file:
            print(file.read())
    except FileNotFoundError:
        print("That file was not found")
    except Exception:
        print("Error occurred! Please check again.")

def write():
    text = input("Write:\n")
    style = input("Overwrite (O) or Append (A): ").upper()
    try:
        if style == "O":
            with open("write", 'w') as file:
                file.write(text)
        elif style == "A":
            with open("write", 'a') as file:
                file.write(text)
        else:
            print("Something went wrong....")
    except Exception as e:
        print(f"Error occurred: {e}")

def copy():
    origin = input("Enter a file to copy: ")
    copy = input("Save this file name as: ")
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

def move():
    soc = input("Enter a file to move: ")
    des = input("Move this file to: ")
    try:
        if os.path.exists(des):
            print("There is already a file there")
        else:
            os.replace(soc, des)
            print(f"{soc} was moved successfully.")
    except FileNotFoundError:
        print(f"{soc} was not found")

def delete():
    delete = input("Enter a file to delete: ")
    try:
        if os.path.isdir(delete):
            shutil.rmtree(delete)
            print(f"{delete} was deleted.")
        elif os.path.isfile(delete):
            os.remove(delete)
            print(f"{delete} was deleted.")
    except FileNotFoundError:
        print("There is no file.")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Error occurred: {e}")

def main_menu():
    options = {
        'find': find,
        'read': read,
        'write': write,
        'copy': copy,
        'move': move,
        'delete': delete
    }

    running = True
    while running:
        method = input("Find/Read/Write/Copy/Move/Delete: ").lower()
        if method in options:
            options[method]()  # Call the corresponding function
        else:
            print("Type again carefully!")

        if not input("Enter R to try again/Press any other key to quit: ").upper() == "R":
            running = False
            print("See ya again...")

if __name__ == "__main__":
    main_menu()
