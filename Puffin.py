import click
import sys
import os
import mpmath as mp

from antlr_control import antlr_python, antlr_puffin
from useful import getSigFig

sys.tracebacklimit = 0
## Define errors
class Errm(Exception):
    pass

def method1(file,puffin,output,language):

    puffin_ = puffin+language

    antlr_puffin.read(puffin,puffin_,language)

    if language == 'python':
        antlr_python.write(file,output,puffin_)

    # Try to delete temp files
    # try: os.remove(puffin_)
    # except: pass


def method2(file,output,language):

    if language == 'python':
        antlr_python.read(file,output)


def method3(file,output,language):

    puffin = 'temp.pf'
    puffin2 = 'temp2.pf'
    puffin_ = 'temp.pf_'

    if language == 'python':
        antlr_python.read(file,puffin)
        method4(puffin,puffin2)
        antlr_puffin.read(puffin2,puffin_,language)
        antlr_python.write(file,output,puffin_)

    # Try to delete temp files
    try:
        os.remove(puffin)
        os.remove(puffin2)
        os.remove(puffin_)
    except: pass


def method4(puffin,output):

    vars = [line for line in open(puffin,'r')]
    new_vars = ""
    for var in vars:

        if var != "":
            i = var.split('->')[1]
            try:

                mp.mpf(i)
                lower,higher = getSigFig(i)
                interval = "[%s,%s]" %(lower,higher)

                new_vars+=var.replace(i,interval)+'\n'

            except: new_vars+=var+'\n'
        else:
            new_vars+=var+'\n'

    with open(output,'w') as f:
        print(new_vars,file = f)

def method5(file,output,language):

    temp = 'temp.pf'
    method2(file,temp,language)
    method4(temp,output)

    try:
        os.remove(temp)
    except: pass

@click.command()

@click.option('--file',default = None,help='Input File')
@click.option('--output',default = None, help='Output file')
@click.option('--auto', flag_value=True,type = bool ,help = 'Automatically create intervals')
@click.option('--puffin', default = None, help = 'Input puffin file')
@click.option('--getpf',flag_value=True,type = bool ,help = 'Create puffin language file from input file')
def puffinComp(file,output,puffin,getpf,auto):
    '''Uncertainty Compiler'''

    # Find what the user is trying to do or raise an error
    if file is None:

        if puffin is None:

            raise Errm("\nI can\'t do anything without input files")

        elif not auto:

            raise Errm("\nI was expecting --auto=True")

        else:
            method = 4

    else:

        if puffin is None and not getpf and not auto:

            raise Errm("\nI don\'t know what you want me to do")

        elif puffin is None and getpf and auto:

            method = 5

        elif puffin is None and getpf and not auto:

            method = 2

        elif puffin is None and auto and not getpf:

            method = 3

        elif puffin is not None and auto:

            raise Errm("\nI wasn\'t expecting --auto=True\nTry without?")

        elif puffin is not None and getpf:

            raise Errm("\nI wasn\'t expecting --getpf=True\nTry without?")

        elif puffin is not None and not getpf and not auto:

            method = 1

        else: raise Errm("I give up")


    if method in (1,2,3,5):

        fileName, fileExt = file.split('.')

        if output is None:
            if getpf:
                output = fileName +'.pf'
            else:
                output = file.replace('.','_pf.')

        if fileExt == 'py':
            language = 'python'
        else:
            raise Errm('I don\'t know that language!')

        if method == 1:

            method1(file,puffin,output,language)

        elif method == 2:

            method2(file,output,language)

        elif method == 3:

            method3(file,output,language)

        elif method == 5:

            method5(file,output,language)

    else:

        if output is None:

            output = puffin.replace('.','2.')

        method4(puffin,output)



if __name__ == '__main__':
    puffinComp()
