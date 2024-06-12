## Atlas AirBnB Clone - The Console Project
![Console logo](https://github.com/LJThao/atlas-AirBnB_clone/blob/main/images/console.png)

## Description
This command-line tool is made for an Airbnb-like app. It lets you interact with the app's backend through simple commands in a console. You can create, update, and delete things in the app's database with ease. It's also a handy way to test and make sure the storage system works well.

## Installation
First, clone the repository:

```
$ git clone https://github.com/LJThao/atlas-AirBnB_clone.git
```

Next, go to the atlas-AirBnB_clone directory:

```
$ cd atlas-AirBnB_clone
```
## How to use it?
Start the console by entering `./console.py`. Then, this will start the command line interpreter and you will be prompted with `(hbnb)`...
Here are the available commands:

* `EOF` - Exit the console
* `all` - Print the string representations of all of the instances of classes
* `create` - Create a new instance
* `destroy` - Delete an instance
* `help` - Help settings
* `quit` - Exit the console
* `show` - Print the string representation of the instance
* `update` - Update an instance

## Interactive mode & Examples:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Non-interactive mode & Examples:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```

## Tests for Interactive and Non-interactive mode:
```
python3 -m unittest discover tests
$ echo "python3 -m unittest discover tests" | bash
```

## Authors and Acknowledgments

* `LJ Thao`
* `Dacoda Takagi` 
* `Charles Johnson`

![HBHB logo](https://github.com/LJThao/atlas-AirBnB_clone/blob/main/images/airbnb.png)

