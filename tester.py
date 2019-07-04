from antlr_control import *
import click

def Python3():

    # antlr_Python3.read('test.py','test.uq')
    antlr_puffin.read('test.uq','test.uq-py','Python3')
    antlr_Python3.write('test.py','test_uq.py','test.uq-py')

def uq():
    antlr_puffin.read('test.uq','test.uq-py','Python3')

@click.command()

@click.option('--language',default = None,help = 'Language ')
def main(language):

    if language == None:
        print('Select Language\n\nEnter 1 for Python\nEnter 2 for uq\n\n')
        n = input('')

        if n == '1':
            language = 'Python3'
        elif n == '2':
            language = 'uq'


        if language == 'Python3':
            Python3()
        elif language == 'uq':
            uq()

if __name__ == '__main__':
    main()
