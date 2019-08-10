# FolderDatabase
Easy folder indexing w/o DB for all file system.\
Creating a system that allows the organization of a directory tree without using a real database or a complicate application, in case of need can be surfed in plain text, without launching the script. Everything is base on hidden file inside each leaf of the directory tree. The script can scan for new folder, without a description, search between descriptions and all the other functions related to the managed of this NoDB.

## Usage
The script require some additional libraries from pip3. They can be installed via:
```
pip3 install -r requirements.txt
```
The script can then be run using the command:
```
python3 main.py directory_tree_root
```

## How it works
The script make use of hidden files inside each "final" folder. A final folder is a leaf of a directory tree, a folder containing only files and no more folders.\
Supposing to have a directory tree of this type:
```
test
├── 2016
│   ├── 02
│   │   ├── 02
│   │   │   ├── file001.bin
│   │   │   ├── file002.bin
│   │   │   └── file003.bin
│   │   ├── 03
│   │   │   └── file001.bin
│   │   └── 04
│   │       ├── file001.bin
│   │       ├── file002.bin
│   │       └── file003.bin
│   └── 03
│       ├── 13
│       │   └── file001.bin
│       └── 15
│           ├── file001.bin
│           ├── file002.bin
│           └── file003.bin
├── 2018
│   └── 12
│       └── 1
│           ├── file012.bin
│           └── file016.bin
└── 2019
    └── file001.bin

12 directories, 14 files
```
On each of the folder on the lowest level of the tree a bookmark can be added in order to keep additional information about that folder, it can be useful for managing photos or videos archive.\\
One .info file will be added like bookmark, the file remain visible and made os plain-text (ASCII), this allows also a navigation without the necessity of this script, can be used directly from system without python available for example.
These file will contains 2 lines:
```
One line with de description fields
Another,line,with,keyword,list
```
The script can be used in order to improve the graphical visualization of this stuffs and to allows also search among that fields. The output will be like this:
```
+------------+--------------+--------------+---------+
| Folder     | Description  | Keywords     | # Files |
+------------+--------------+--------------+---------+
| 2016/02/02 | First entry  | first,entry  | 3       |
| 2016/02/04 | Second entry | second,entry | 3       |
| 2016/03/15 | Third entry  | third,entry  | 3       |
+------------+--------------+--------------+---------+
```

## Built With

* [Python 3](https://www.python.org/) - The development language

## Authors
* **Jacopo Nasi** - [Jacopx](https://github.com/Jacopx)