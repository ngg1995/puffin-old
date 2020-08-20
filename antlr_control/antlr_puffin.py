import sys
from antlr4 import *
from languages.puffin import puffinParser, puffinLexer, puffinListener

def read(input,target = "Python3"):
    # input = FileStream(filename,encoding='utf-8')
    lexer = puffinLexer(input)
    stream = CommonTokenStream(lexer)
    parser = puffinParser(stream)
    tree = parser.file_input()


    puffin = puffinListener(target)
    walker = ParseTreeWalker()
    walker.walk(puffin, tree)


    return puffin.uncerts, puffin.changes, puffin.dependencies

if __name__ == "__main__":
    read('test.pf','test.pf-py','python')
