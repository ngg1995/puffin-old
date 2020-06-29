from antlr4 import *
from antlr_control import *
import sys

args = sys.argv[1]

input = InputStream(args)
output = antlr_Python3.read(input)

print(output)
