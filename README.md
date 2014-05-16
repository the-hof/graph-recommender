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

