import sys
from antlr4 import *
from languages.R import RLexer, RParser, RWriter, RReader

import os

def read_uncert(file):
    uncerts = {}
    changes = {}
    with open(file,'r') as f:
        for line in f:
            if line.strip() != "":
                parts = [x.strip() for x in line.split('->')]

                if '«' in line:

                    changes[parts[0].replace("«",'').replace("»","")] = parts[1]
                else:

                    uncerts[parts[0]] = parts[1]

    return uncerts,changes



def write(filename,newName,uncerts_file):

    input = FileStream(filename,encoding='utf-8')
    lexer = RLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RParser(stream)
    tree = parser.file_input()


    uncerts,changes = read_uncert(uncerts_file)

    output = open(newName,"w")

    RPuffin = RWriter(output,uncerts,changes = changes)
    walker = ParseTreeWalker()
    walker.walk(RPuffin, tree)

    output.close()

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

if __name__ == "__main__":

    import antlr_puffin

    # read('test.py','test.pf')
    antlr_puffin.read('test.pf','test.pf-R','R')
    write('test.R','test_puffin.R','test.pf-R')
