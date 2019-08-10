# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *                             FolderDatabase                              *
# *                https://github.com/Jacopx/FolderDatabase                 *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                        usage: main.py db_tree_root                        *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
import sys
import os
from prettytable import PrettyTable


def clear():
    os.system('clear')


def print_menu():
    clear()  # This function not work inside the IDE console
    print(30 * "-", "MENU", 30 * "-")
    print("1. Show tree")
    print("2. Add bookmark")
    print("3. -----")
    print("4. Delete Bookmark")
    print("5. Exit")
    print(67 * "-")


def menu(root_dir="."):

    # Text menu in Python
    loop = True

    while loop:
        print_menu()
        choice = input("Enter your choice [1-5]: ")

        if choice != '' and choice.isdecimal():
            choice = int(choice)
        else:
            continue

        if choice == 1:
            tree(root_dir)
        elif choice == 2:
            add(root_dir)
        elif choice == 4:
            delete(root_dir)
        elif choice == 5:
            print("Exiting from software, bye!")
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


def tree(root_dir="."):
    print_tree(root_dir)
    input("\nClose? ")


def print_tree(root_dir="."):
    t = PrettyTable(["Folder", "Description", "Keywords", "#Files"])
    t.align["Folder"] = "l"
    t.align["Description"] = "l"
    t.align["Keywords"] = "l"
    t.align["#Files"] = "l"
    for dirName, subdirList, fileList in os.walk(root_dir):
        if len(fileList) > 0:
            for fname in fileList:
                if fname == ".info":
                    f = open(dirName + "/.info")
                    descr = f.readline()
                    keyword = f.readline()
                    f.close()
                    t.add_row([dirName[len(root_dir) + 1:], descr[:len(descr) - 1], keyword, len(fileList)])
    print(t)


def add(root_dir="."):
    x = PrettyTable(["Folder", "Description", "Keywords", "#Files"])
    x.align["Folder"] = "l"
    x.align["Description"] = "l"
    x.align["Keywords"] = "l"
    x.align["#Files"] = "l"

    for dirName, subdirList, fileList in os.walk(root_dir):
        bookmark = False
        if len(fileList) > 0:
            for fname in fileList:
                if fname.startswith("."):
                    bookmark = True
            if not bookmark:
                x.add_row([dirName[len(root_dir)+1:], "", "", len(fileList)])

    print(x)
    path = input("Insert the path to the folder to be indexed: ")

    f = open(root_dir + "/" + path + "/.info", "w")
    descr = input("Insert description: ")
    keyword = input("Insert keyword: ")
    f.write(descr)
    f.write("\n")
    f.write(keyword)
    f.close()


def delete(root_dir="."):
    print_tree(root_dir)
    path = input("Which bookmark delete: ")
    os.remove(root_dir + "/" + path + "/.info")
    print("Bookmark removed!")
    input("\nClose? ")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        menu(sys.argv[1])
    else:
        menu()
