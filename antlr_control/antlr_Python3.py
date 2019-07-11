import sys
from antlr4 import *
from languages.Python3 import Python3Lexer, Python3Parser, Python3Writer, Python3Reader

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
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()


    uncerts,changes = read_uncert(uncerts_file)

    output = open(newName,"w")

    Python3Puffin = Python3Writer(output,uncerts,changes = changes)
    walker = ParseTreeWalker()
    walker.walk(Python3Puffin, tree)

    output.close()

def read(filename,outfile):
    input = FileStream(filename,encoding='utf-8')
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

    output = open(outfile,"w")

    Python3Puffin = Python3Reader(output)
    walker = ParseTreeWalker()
    walker.walk(Python3Puffin, tree)

    output.close()

if __name__ == "__main__":

    import antlr_puffin

    # read('test.py','test.pf')
    antlr_puffin.read('test.pf','test.pf-py','Python3')
    write('test.py','test_puffin.py','test.pf-py')
