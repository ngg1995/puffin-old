from antlr4 import *
from antlr_control import *
import sys

source = InputStream(sys.argv[1])
puffin = InputStream(sys.argv[2])
language = "Python3"

uncerts,changes,dependencies = antlr_puffin.read(puffin,language)

if language == 'Python3':
    output = antlr_Python3.write(source,uncerts,changes,dependencies)
elif language == 'R':
    output = antlr_R.write(source,uncerts,changes)

print(output)
