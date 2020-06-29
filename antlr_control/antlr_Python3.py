import sys
from antlr4 import *
from languages.Python3 import Python3Lexer, Python3Parser, Python3Writer, Python3Reader
from useful import read_uncert
import os



def read(input):
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

    # output = open(outfile,"w")

    Python3Puffin = Python3Reader()
    walker = ParseTreeWalker()
    walker.walk(Python3Puffin, tree)

    return Python3Puffin.output

def write(input,uncerts,changes,dependencies):

    # input = FileStream(filename,encoding='utf-8')
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()


    Python3Puffin = Python3Writer(uncerts = uncerts,changes = changes,dependencies = dependencies)
    walker = ParseTreeWalker()
    walker.walk(Python3Puffin, tree)


    return Python3Puffin.output
    # if Python3Puffin.varlist != []:
    #     print("No matches could be found for the following variables:")
    #     for v in Python3Puffin.varlist:
    #         print('\t%s'%v)
    # output.close()

if __name__ == "__main__":

    import antlr_puffin

    # read('test.py','test.pf')
    antlr_puffin.read('test.pf','test.pf-py','Python3')
    write('test.py','test_puffin.py','test.pf-py')
