# Task 3: Installing Python, VS Code, and a virtual env on your PC Computer

In this class, we will be teaching you Python programming from the ground up! The best way to learn Python is by practicing as often as you can. By installing python directly on your laptop, you can practice anywhere and anytime you like, with or without an internet connection.

## Getting Started, Installing WSL and Ubuntu on your PC

Before we can get started, we need to install a basic Unix Operating System on your Windows machine. Windows Subsystem for Linux (WSL) comes with the Windows operating system, but you must enable it and install a Linux distribution (Ubuntu) before you can begin using it. This will allow you to use basic Unix commands in this class including "chmod" for making your python scripts executable, and "make test" to run the tests on your python code to make sure the code is correct.

* Make sure your laptop has been recently updated and has the most recent Windows Updates.
* Use this[tutorial](https://code.visualstudio.com/docs/remote/wsl-tutorial) to install WSL and an Ubuntu distribution (first two sections).
* Be sure to create a user / password for Ubuntu

If you have any trouble, here are a few extra links from the Microsoft website on WSL installation:

* [Getting started](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#get-started})
* [Set up your Linux Username and Password](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)

## Installing Python and the Python Virtual Environment on your Ubuntu distribution

Now that you have Ubuntu installed on your PC, you need to install the version of Python that we will be using for the class (Python 3.11.1). Note that Python version 3.10 comes with the Ubuntu installation. To install the latest Python, you will launch the Ubuntu app and use the following commands to install Python 3.11.1:

```
sudo apt install python3.11.1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sudo update-alternatives --config python3
sudo apt install python3.11-venv
sudo apt install python3-pip
```

You can now check the installation to see where Python is installed and which version you have.

```
which python3
python3 --version
```

These commands above should return the following:
```
/usr/bin/python3
Python 3.11.0rc1
```

You will also need to update your $PATH to tell your computer where to find Python.

```
touch ~/.profile
nano ~/.profile
```

Add this line to the ~/.profile file when the nano file editor opens it.

```
export PATH="~/.local/bin:$PATH"
```

## Getting started with the VS Code Editor

Code editors (or Integrated Development Environment, IDEs) are fantastic resources that make it easy to write and edit code on your laptop. There are many code editors out there, but in this class, we will be using the VS Code editor to write and edit our Python programs. Code editors recognize the programming language we are coding in and highlight the syntax of the code making it easier to "see". In addition, code editors offer code completion options and can even suggest a Pytnon function for you to use based on a few letters. Amazing! IDEs will definitely make your life easier! I recommend learning as much as you can about VS Code to find out its capabilities and how it can help you in writing great code. For now, here are a few instructions to get you started.

### Step 1: Install VScode

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop. We will write and edit python code using the Visual Studio code editor. Follow the directions on the VS Code website to download and install the version of [VS Code](https://code.visualstudio.com/) that is appropriate for your PC laptop.

* You must install VS code by downloading and installing the application on your laptop from the link above. Installing VS Code through Ubuntu (not shown here) will result in incorrect paths, and trouble down the road with finding unix commands and the python installation.

### Step 2: Install the Python extensions for VS Code

Once VS Code is installed you will need to install an extension for Python. VS Code can be used for programming in many different programming languages, so we will need to tell VSCode that we want to use Python. You can learn more about extensions [here](https://code.visualstudio.com/docs/introvideos/extend).

To install the Python extension, go the the VS Code menu, Select View -> Extensions, to pull up the "Extensions Market Place" on the left-hand panel. Search for and install "Python" by IntelliSense. This extension works alongside Python in Visual Studio Code to provide performant language support, linters, and debuggers for Python. You will learn about each of these in the days to come. They will be useful in formatting your code to make it beautiful, while also checking for mistakes and errors.

### Step 3: Tell VScode which version of Python to use

Next, we need to tell VScode which version of Python to use, and point to the latest version that we just installed. To do this, you can go to View -> Command Palette. Then in the search box type "Python: Select Interpreter". Choose the most recent version of python that you just installed 3.11.1. Now you are all set to start writing Python code in VS Code!

### Step 4: Setting up a virtual environment in VS code

When you installed Python on your computer you installed it globally on the Ubuntu Linux distribution. But, working in a global environment can be tricky because different versions of python packages may not play nicely together. To avoid any conflicts, developers usually create a virtual environment for each project and then install the packages they need in that virtual environment. When you then run a Python program within that environment, you know that it's running against only those specific packages.

We are going to create a virtual environment in VS Code for our class. We will install several python packages/modules that will help us to test, debug and format our code in this virtual environment.

* From the VS Code menu bar select File -> Open Folder -> Then navigate to the be433-spring-2023 folder that you "pulled" down to your computer from GitHub.

Next, we will create a virtual environment (venv) in VS Code to install all of the Python packages we will need for our class. venv allows you to manage separate package installations for different projects and is installed with Python 3 by default.

* From within VS Code, you can create non-global environments, using virtual environments by opening the Command Palette, start typing "Python: Create Environment command" to search, and then select the command.

The command presents a list of environment types: Venv or Conda. Select Venv.
![1venv](./images/1_venv_select_env_type.png "Selecting a venv type")

The the command presents a list of interpreters that can be used as a base Python for the new virtual environment. Select Python Version 3.11.1 that we just installed.
![2venv](./images/2_venv_select_python_version.png "Selecting a venv python version")

### Step 5: Install the Python modules we need for this class in the venv

Once you have created your vitual environment, you can install Python modules in that environment. In Python, modules are how you obtain any number of useful code libraries. For example, in this class we will use several modules that will help us to test, debug and format code. These are all contained in the requirement.txt file in the docs directory in the be434-spring-2023 Github repository.  

First we need to open a terminal window in VS Code:
![3venv](./images/vscode_open_terminal.png "Opening a terminal in VS Code")

Note, you should already have the be434-spring-2023 directory open in VS Code and it should automatically activate the virtual environment when you open the terminal
![4venv](./images/3_venv_activate_env.png "Activating a virtual environment")

If this is not the case, be sure to open the be434-spring-2023 directory in VS Code and then activate the virtual machine

You will need to enter the following commands in the terminal:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
source .venv/bin/activate
```

Now you can install the python modules we need into your virtual environment. You can do this with a single command (from the be343-spring-2023 folder):

```
python3 -m pip install -r ./docs/requirements.txt
```

Or by installing each one individually...

```
python3 -m pip install pytest
python3 -m pip install pylint
python3 -m pip install flake8
python3 -m pip install yapf
python3 -m pip install black
python3 -m pip install mypy
python3 -m pip install pytest-flake8
python3 -m pip install pytest-mypy
python3 -m pip install pytest-pylint
```

Overview of these commands:

```
black # this command will format our code properly
pytest # this command will test our code with default test discovery mechanism.
mypy # this command will run type checks on our code with mypy.
flake8 # this command will check code linting.
```

### Step 6: Fixing a small issue with pylint

Now you have installed all of the python modules that we need for testing your code! Congrats! When we start testing our code (in the weeks to come), you might find that "pylint" complains about the variable `rv` (return value) that is in the _test.py_ file of each homework. This is a perfectly fine variable name, so to silence this warning, create your own configuration file like so:

```
pylint --generate-rcfile > ~/.pylintrc
```

Then edit that file to add the following line after "MAIN". Note that this should be one continuous line, but I've broken it here for display:

```
disable=too-many-locals,invalid-name,too-many-statements,too-many-arguments,cell-var-from-loop,wrong-import-order
``` 

```
nano ~/.pylintrc
```
Use ctr-O & return to save the file, and ctr-X to exit

## Author

Bonnie Hurwitz <bhurwitz@arizona.edu>