# How to use Guide


# Uncertainty Compiler - How to use


## 0. Install python [www.python.org](https://www.python.org/)
Puffin (*at the moment*) requires you to be able to use python3 from unix terminal or windows command prompt

## 1. Download puffin
###If git installed

    git clone https://gitlab.com/nickgray1995/puffin-compiler.git

###If git not installed

Download from gitlab directly and unzip

## 2. Download required python files using pip

    pip install puffin-python-library

You may have to use the --user tag at the end of the command

## 3. Create short names
This step is optional but you may find useful
### UNIX

    alias puffin="python3 puffin.py"

### Windows
3b. Create batch file in windows with the following in

    @echo off
    python puffin.py %1 %2 %3 %4

## 4. Use in command line

To compiler uncertainty defined by uncerts.pf into file.py

    puffin --file=file.py --puffin=uncerts.f

To create puffin file from file.py

    puffin --file=file.py --getpf

To automatically add uncertainty based on significant figures

    puffin --file=file.py --auto

    puffin --puffin=uncerts.puffin --auto

output file name can be specified by using

    --output=*whatever.whtevr*
