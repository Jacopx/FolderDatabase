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

## Built With

* [Python 3](https://www.python.org/) - The development language

## Authors
* **Jacopo Nasi** - [Jacopx](https://github.com/Jacopx)