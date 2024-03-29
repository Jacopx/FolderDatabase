# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *                             FolderDatabase                              *
# *                https://github.com/Jacopx/FolderDatabase                 *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                        usage: main.py db_tree_root                        *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
import sys
import os
from prettytable import PrettyTable
import operator


def clear():
    os.system('clear')


def print_menu():  # Printing menus
    clear()
    print(30 * "-", "MENU", 30 * "-")
    print("1. Show tree")
    print("2. Add bookmark")
    print("3. Edit bookmark")
    print("4. Delete Bookmark")
    print("5. Search Bookmark for description")
    print("6. Search Bookmark for keywords")
    print("7. Exit")
    print(67 * "-")


def menu(root_dir="."):  # Managing user choice and invoke proper functions

    # Text menu in Python
    loop = True

    while loop:
        print_menu()
        choice = input("Enter your choice [1-7]: ")

        if choice != '' and choice.isdecimal():
            choice = int(choice)
        else:
            continue

        if choice == 1:
            tree(root_dir)
        elif choice == 2:
            add(root_dir)
        elif choice == 3:
            edit(root_dir)
        elif choice == 4:
            delete(root_dir)
        elif choice == 5:
            sdescr(root_dir)
        elif choice == 6:
            skeyword(root_dir)
        elif choice == 7:
            print("Exiting from software, bye!")
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


def tree(root_dir="."):
    print_tree(root_dir)
    input("\nClose? ")


def print_tree(root_dir="."):  # 1st choice of the menu to show the database
    t = PrettyTable(["Folder", "Description", "Keywords", "# Files"])
    t.align["Folder"] = "l"
    t.align["Description"] = "l"
    t.align["Keywords"] = "l"
    t.align["# Files"] = "l"
    for dirName, subdirList, fileList in os.walk(root_dir):
        if len(fileList) > 0:
            for fname in fileList:
                if fname == ".info":
                    f = open(dirName + "/.info")
                    descr = f.readline()
                    keyword = f.readline()
                    f.close()
                    t.add_row([dirName[len(root_dir) + 1:], descr[:len(descr) - 1], keyword, len(fileList)])
    print(t.get_string(sort_key=operator.itemgetter(1, 0), sortby="Folder"))


def add(root_dir="."):  # 2nd adding a new bookmark on the database
    x = PrettyTable(["Folder", "# Files"])
    x.align["Folder"] = "l"
    x.align["#Files"] = "l"

    for dirName, subdirList, fileList in os.walk(root_dir):
        bookmark = False
        if len(fileList) > 0:
            for fname in fileList:
                if fname.startswith(".info"):
                    bookmark = True
            if not bookmark:
                x.add_row([dirName[len(root_dir)+1:], len(fileList)])

    print(x.get_string(sort_key=operator.itemgetter(1, 0), sortby="Folder"))
    path = input("Insert the path to the folder to be indexed: ")

    f = open(root_dir + "/" + path + "/.info", "w")
    descr = input("Insert description: ")
    keyword = input("Insert keyword: ")
    f.write(descr)
    f.write("\n")
    f.write(keyword)
    f.close()


def edit(root_dir="."):  # 3rd Editing and existing bookmark
    print_tree(root_dir)
    path = input("Which bookmark edit: ")

    # Reading old file infos
    f_old = open(root_dir + "/" + path + "/.info")
    descr_old = f_old.readline()
    keyword_old = f_old.readline()
    f_old.close()

    #  Delete old file
    os.remove(root_dir + "/" + path + "/.info")
    f = open(root_dir + "/" + path + "/.info", "w")

    # Show old text and waiting for edits, if enter pressed values remain unchanged
    print("[" + descr_old[:len(descr_old)-1] + "]")
    descr = input("Insert description: ")
    if len(descr) == 0:
        descr = descr_old[:len(descr_old)-1]

    print("[" + keyword_old + "]")
    keyword = input("Insert keyword: ")
    if len(keyword) == 0:
        keyword = keyword_old

    f.write(descr)
    f.write("\n")
    f.write(keyword)
    f.close()


def delete(root_dir="."):  # 4th Delete an existing bookmark
    print_tree(root_dir)
    path = input("Which bookmark delete: ")
    os.remove(root_dir + "/" + path + "/.info")
    print("Bookmark removed!")
    input("\nClose? ")


def sdescr(root_dir="."):  # 5th Search by description field
    descr = input("Insert description to search for: ")

    t = PrettyTable(["Folder", "Description", "Keywords", "# Files"])
    t.align["Folder"] = "l"
    t.align["Description"] = "l"
    t.align["Keywords"] = "l"
    t.align["# Files"] = "l"
    for dirName, subdirList, fileList in os.walk(root_dir):
        if len(fileList) > 0:
            for fname in fileList:
                if fname == ".info":
                    found = False
                    f = open(dirName + "/.info")
                    descr_read = f.readline()
                    if descr in descr_read:
                        found = True
                    keyword_read = f.readline()
                    f.close()
                    if found:
                        t.add_row([dirName[len(root_dir) + 1:], descr_read[:len(descr_read) - 1], keyword_read, len(fileList)])
    print(t.get_string(sort_key=operator.itemgetter(1, 0), sortby="Folder"))


def skeyword(root_dir="."):
    keyword = input("Insert keywords to search for: ")

    t = PrettyTable(["Folder", "Description", "Keywords", "# Files"])
    t.align["Folder"] = "l"
    t.align["Description"] = "l"
    t.align["Keywords"] = "l"
    t.align["# Files"] = "l"
    for dirName, subdirList, fileList in os.walk(root_dir):
        if len(fileList) > 0:
            for fname in fileList:
                if fname == ".info":
                    found = False
                    f = open(dirName + "/.info")
                    descr_read = f.readline()
                    keyword_read = f.readline()
                    if keyword in keyword_read:
                        found = True
                    f.close()
                    if found:
                        t.add_row([dirName[len(root_dir) + 1:], descr_read[:len(descr_read) - 1], keyword_read, len(fileList)])
    print(t.get_string(sort_key=operator.itemgetter(1, 0), sortby="Folder"))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        menu(sys.argv[1])
    else:
        menu()
