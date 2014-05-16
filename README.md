graph-recommender
=================

recommendation engine using a graph database

Setting up your Python development environment
------------

The first step is setting up your development environment.  We're going to be doing work with Python so you'll want to set that up.  If you're working on a Mac, you might want to install homebrew (you can find what you need at http://brew.sh/ ) which is a good package manager for OS X.  You also may want an IDE to help manage the code files.  If there's already one that you like, use that.  If you're new to python a suggestion would be PyCharm (free community edition available at http://www.jetbrains.com/pycharm/download/index.html)

On a mac, you can use homebrew to install python 2 or python 3:

    $ brew install python --with-brewed-openssl

or 

    $ brew install python3 --with-brewed-openssl

Setting up source control
------------

You'll want to install git to use for source control.

Installing Virtualenv
------------

Virtualenv is a very useful tool for python development.  It allows each project to have its own environment, setup, and dependencies.  You should have pip installed (pip is a python package manager.  easy_install is another one, but pip is the better maintained one)

    $ pip install virtualenv

Getting the source code for this project using git
------------

Switch to the directory that you use as your workspace.  I typically create a folder under my root called "projects" and each project gets its own subfolder underneath that.  If you have your own preference, use that.

    $ git clone https://github.com/the-hof/graph-recommender.git

This will create a new folder called "graph-recommender" and download the latest code into it.

Making a virtual environment for the project
------------

To create a virtual environment (you'll only do this once per project), do this:

$ virtualenv graph-recommender

you'll see it installing pip and setuptools, just let it do what it wants.

Next you'll want to actually go into the virtual environment:

    $ cd graph-recommender
    $ source bin/activate

The activate script takes all the necessary steps to keep your python project self-contained.  You'll see (graoh-recommender) as part of your command line, that's how you know you're in a virtual environment.  Note that you'll need to do "source bin/activate" each time you open a new terminal.  It doesn't remember from one terminal session to the next that you were in a virtual environment.

Install dependencies
------------

    $ pip install -r requirements.txt

