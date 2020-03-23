import sys
from antlr4 import *
from languages.R import RLexer, RParser, RWriter, RReader

import os

from useful import read_uncert



def read(filename,outfile):
    input = FileStream(filename,encoding='utf-8')
    lexer = RLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RParser(stream)
    tree = parser.file_input()

    output = open(outfile,"w")

    RPuffin = RReader(output)
    walker = ParseTreeWalker()
    walker.walk(RPuffin, tree)

    output.close()

def write(filename,newName,uncerts, changes):

    input = FileStream(filename,encoding='utf-8')
    lexer = RLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RParser(stream)
    tree = parser.file_input()

    output = open(newName,"w")

    RPuffin = RWriter(output,uncerts,changes = changes)
    walker = ParseTreeWalker()
    walker.walk(RPuffin, tree)

    if RPuffin.varlist != []:
        print("No matches could be found for the following variables:")
        for v in RPuffin.varlist:
            print('\t%s'%v)

    output.close()

if __name__ == "__main__":

    import antlr_puffin

    # read('test.py','test.pf')
    antlr_puffin.read('test.pf','test.pf-R','R')
    write('test.R','test_puffin.R','test.pf-R')
