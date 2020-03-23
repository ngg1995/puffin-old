import click
import sys
import os
import mpmath as mp

from antlr_control import *
from useful import getSigFig


# sys.tracebacklimit = 0
## Define errors
class Errm(Exception):
    pass

def full_compile(file,puffin,output,language):
    ## Takes a input file and a puffin file and compiler the puffin Uncertainties in to the input file


    uncerts,changes,dependencies = antlr_puffin.read(puffin,language)

    if language == 'Python3':
        antlr_Python3.write(file,output,uncerts,changes,dependencies)
    elif language == 'R':
        antlr_R.write(file,output,uncerts,changes)


    print('Compiled')


def get_puffin(file,output,language):
    # Reads a script and outputs a puffin file
    if language == 'Python3':
        antlr_Python3.read(file,output)
    elif language == 'R':
        antlr_R.read(file,output)

    print('Created puffin file')

def auto_uq_compile(file,output,language):
    # Fully automatic uncertainty compile

    puffin = 'temp.pf'
    puffin2 = 'temp2.pf'


    if language == 'Python3':
        antlr_Python3.read(file,puffin)
        add_in_auto_uq(puffin,puffin2)
        uncerts,changes,dependencies = antlr_puffin.read(puffin2,language)
        antlr_Python3.write(file,output,uncerts,changes,dependencies)

    elif language == 'R':
        antlr_R.read(file,puffin)
        add_in_auto_uq(puffin,puffin2)
        uncerts,changes,dependencies = antlr_puffin.read(puffin2,language)
        antlr_R.write(file,output,uncerts,changes)

    # Try to delete temp files
    try:
        os.remove(puffin)
        os.remove(puffin2)

    except: pass

def add_in_auto_uq(puffin,output):
    # Adds automatic uncertainty to puffin file
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

    print('Automatically calculated uncertainty')

def output_auto_script(file,output,language):
    # outputs puffin file with auto uq
    temp = 'temp.pf'
    get_puffin(file,temp,language)
    add_in_auto_uq(temp,output)

    try:
        os.remove(temp)
    except: pass

def user_control():

    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'. WHICH STILL DOESNT WORK
        directory = os.path.dirname(sys.argv[0])
    else:
        directory = os.path.dirname(os.path.abspath(__file__))

    running = True
    file = None
    puffin = None
    language = None
    output = None
    file_long = None
    puffin_long = None
    output_long = None

    infolder = os.listdir(directory)

    # Change to current folder
    os.chdir(directory)

    if sys.platform.startswith('darwin'):
        os.system('clear')

    print('Welcome to Puffin\n\n')
    print('Working directory: '+directory)
    print('To enter input script:  \"file=filename\"')
    print('To enter puffin script: \"puffin=filename\"')
    print('To specify language: \"language=language\" \n')
    print('Entering \"output = name\" define a output name')
    print('To compile puffin script into input script: \"compile\"')
    print('To compile using automatic uncertainty analysis: \"auto\"')
    print('To generate puffin script from input script: \"getpf\"\n')
    print('To get generate puffin script with automatic uncertainty analysis: \"autopf\"')
    print('\";\" can be used to enter multiple commands at once')
    print('i.e. \"file=example.py; puffin=uq.pf; output=name.py; compile\"\n\n')
    print('Entering \"info\" will list all defined files and availible options')
    print('To exit enter \"quit\"\n\n')

    while running:

        line = input('> ')

        commands = line.split(';')

        for command in commands:

            command = command.strip()

            if command == 'quit':
                #Stop running
                running = False


            elif command.startswith('file'):
                # Find filename
                try:

                    file = command.split('=')[1].strip()
                    print('Loaded: '+file)
                    file_long = directory + '/' + file

                except:
                    print('Can\'t detect filename')

            elif command.startswith('puffin'):
                # Find puffin file name
                try:

                    puffin = command.split('=')[1].strip()
                    print('Loaded: '+puffin)
                    file_long = directory + '/' + puffin

                except:

                    print('Can\'t detect puffin filename')

            elif command.startswith('language'):
                # Find language
                try:

                    language = command.split('=')[1].strip()

                except:

                    print('Can\'t detect language')

            elif command.startswith('output'):
                # Find language
                try:

                    output = command.split('=')[1].strip()

                except:

                    print('Can\'t detect output name')

            elif command == 'compile':

                if file is None:
                    # Cannot compile if no input file
                    print('ERROR: No input file')
                elif puffin is None:
                    # Cannot compile if no puffin file
                    print('ERROR: No puffin file')
                else:

                    # If no output file need to make one
                    if output is None:
                        output = file.replace('.','_pf.')

                    # If no entered language then need to define one
                    if language is None:
                        fileName, fileExt = file.split('.')
                        fileExt = fileExt.lower()
                        if fileExt == 'py':
                            language = 'Python3'
                        elif fileExt == 'r':
                            language = 'R'
                        else:
                            print('ERROR: I don\'t know the language')

                    if language is not None:
                        # Can do compiles
                        full_compile(file,puffin,output,language)
                        print('Compiled')

            elif command == 'getpf':

                if file is None:
                    # Cannot compile if no input file
                    print('ERROR: No input file')

                else:
                    fileName, fileExt = file.split('.')
                    fileExt = fileExt.lower()
                    if language == None:
                        if fileExt == 'py':
                            language = 'Python3'
                        elif fileExt == 'r':
                            language = 'R'
                        else:
                            print('ERROR: I don\'t know the language')

                    if output is None:

                        output = fileName +'.pf'

                    if language is not None:
                        # Can get puffin file
                        get_puffin(file,output,language)

                        puffin = output
                        print('Created '+output)

            elif command == 'auto':

                if file is not None:

                    fileName, fileExt = file.split('.')
                    fileExt = fileExt.lower()

                    if language is None:

                        if fileExt == 'py':
                            language = 'Python3'
                        elif fileExt == 'r':
                            language = 'R'
                        else:
                            print('ERROR: I don\'t know the language')

                    if output is None:
                        output = file.replace('.','_pf.')

                    if language is not None:

                        auto_uq_compile(file,output,language)

                elif puffin is not None:

                    if output is None:

                        output = puffin.replace('.','_auto.')

                    add_in_auto_uq(puffin,output)

                else: print("I don\'t know what you want me to do")

            elif command == 'autopf':

                if file is not None and puffin is not None:
                    print('AMBIGUITY WARNING: Will generate auto puffin file from %s not %s' %(file,puffin))
                    print('                   To get from %s use \"autopf-pf\"' %(puffin))

                if file is not None:

                    fileName, fileExt = file.split('.')
                    fileExt = fileExt.lower()

                    if language is None:

                        if fileExt == 'py':
                            language = 'Python3'
                        elif fileExt == 'r':
                            language = 'R'
                        else:
                            print('ERROR: I don\'t know the language')

                    if output is None:
                        output = file.replace('.','_pf.')

                    if language is not None:

                        output_auto_script(file,output,language)

                elif puffin is not None:

                    if output is None:

                        output = puffin.replace('.','_auto.')

                    add_in_auto_uq(puffin,output)

                else: print("I don\'t know what you want me to do")

            elif command == 'info':

                if directory is not None:
                    print('Working directory: '+directory)

                if file is not None:
                    print('file = '+file)
                else:
                    print('No input file')

                if puffin is not None:
                    print('puffin = '+puffin)
                else:
                    print('No puffin language')

                if language is not None:
                    print('language = '+language)
                else:
                    print('Language unknown')

                if output is not None:
                    print('output = '+output)
                else:
                    print('No output name specified')

                print('\nMethods availible:')

                if file is not None and puffin is not None:
                    print('compile')
                    print('getpf')
                    print('auto')
                    print('autopf')
                elif puffin is None and file is not None:
                    print('getpf')
                    print('auto')
                    print('autopf')
                elif file is None and puffin is not None:
                    print('auto')
                    print('autopf')
                else:
                    print('None availible')

            elif command == 'cd':
                directory = ask_dir()

            else: print('ERROR: Unkown command')

@click.command()

@click.option('--file',default = None,help='Input File')
@click.option('--output',default = None, help='Output file')
@click.option('--auto', flag_value=True,type = bool ,help = 'Automatically create intervals')
@click.option('--puffin', default = None, help = 'Input puffin file')
@click.option('--getpf',flag_value=True,type = bool ,help = 'Create puffin language file from input file')
def puffinComp(file,output,puffin,getpf,auto):
    '''Uncertainty Compiler'''

    # Method 1 -> full_compile
    # Method 2 -> get_puffin
    # Method 3 -> auto_uq_compile
    # Method 4 -> add_in_auto_uq
    # Method 5 -> output_auto_script

    # Find what the user is trying to do or raise an error
    if file is None:

        if puffin is None:

            user_control()
            method = 0

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

        fileExt = fileExt.lower()

        if output is None:
            if getpf:
                output = fileName +'.pf'
            else:
                output = file.replace('.','_pf.')

        if fileExt == 'py':
            language = 'Python3'
        elif fileExt == 'r':
            language = 'R'
        else:
            raise Errm('I don\'t know that language!')

        if method == 1:

            full_compile(file,puffin,output,language)

        elif method == 2:

            get_puffin(file,output,language)

        elif method == 3:

            auto_uq_compile(file,output,language)

        elif method == 5:

            output_auto_script(file,output,language)

    elif method == 4:

        if output is None:

            output = puffin.replace('.','_auto.')

        add_in_auto_uq(puffin,output)



if __name__ == '__main__':

    puffinComp()
