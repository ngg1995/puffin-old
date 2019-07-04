import sys
from antlr4 import *
from languages.puffin import puffinParser, puffinLexer, puffinListener

def read(filename,outfile,target):
    input = FileStream(filename,encoding='utf-8')
    lexer = puffinLexer(input)
    stream = CommonTokenStream(lexer)
    parser = puffinParser(stream)
    tree = parser.file_input()

    output = open(outfile,"w")

    puffin = puffinListener(output,target)
    walker = ParseTreeWalker()
    walker.walk(puffin, tree)

    output.close()

if __name__ == "__main__":
    read('test.pf','test.pf-py','python')
