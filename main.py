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
    print("2. -----")
    print("3. -----")
    print("4. -----")
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
        elif choice == 5:
            print("Exiting from software, bye!")
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


def tree(root_dir="."):
    x = PrettyTable(["Folder", "Description", "#Files"])
    x.align["Folder"] = "l"
    x.align["Description"] = "l"
    x.align["#Files"] = "l"
    for dirName, subdirList, fileList in os.walk(root_dir):
        if len(fileList) > 0:
            x.add_row([dirName[len(root_dir)+1:], "", len(fileList)])

    print(x)
    input("\nClose? ")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        menu(sys.argv[1])
    else:
        menu()
