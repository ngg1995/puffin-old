# How to use Guide


# Uncertainty Compiler - How to use


### 0. Install python [www.python.org](https://www.python.org/)


### 1. Check that required modules have been installed correctly

    pip install click

    pip install pyqt5

    pip install mpmath

    pip install numpy


### 2. Run the following to get GUI

    python3 main.py


### 3a. Set alias for command line interface (unix only)

    alias puffin="python3 puffin.py"


### 3b. Use in command line

To compiler uncertainty defined by uncerts.puffin into file.py

    puffin --file=file.py --puffin=uncerts.puffin

To create puffin file from file.py

    puffin --file=file.py --getpf

To automatically add uncertainty based on significant figures

    puffin --file=file.py --auto

    puffin --puffin=uncerts.puffin --auto

output file name can be specified by using

    --output=*whatever.py*
