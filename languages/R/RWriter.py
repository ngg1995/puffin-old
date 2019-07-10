# Generated from R.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

from useful import *

preamble = '''### CODE GENERATED BY PUFFIN

# This code requires pba.r to be sourced
# It must be in the same folder as this script as runtime

library(methods) # Needed to correctly source R files

source('pba.r')

### PRECOMPILED WITH UNCERTAINTY CODE BELOW
'''

# This class defines a complete listener for a parse tree produced by RParser.
class RWriter(ParseTreeListener):

    def __init__(self, output,uncerts = {},translations = {},changes={}):
        self.output = output
        self.uncerts = uncerts
        self.changes = changes
        self.output.write(preamble)
        self.indent = 0
        self.insuite = False
        self.atomcount = 0

    # Exit a parse tree produced by RParser#stmt.
    def exitStmt(self, ctx:RParser.StmtContext):

        if not self.insuite:
            ctx.text = child_catcher(ctx,'R')
            self.output.write(ctx.text+'\n')
        else:
            ctx.text = child_catcher(ctx,'R',indent = self.indent)

        self.atomcount = 0


    # Exit a parse tree produced by RParser#complex_stmt.
    def exitComplex_stmt(self, ctx:RParser.Complex_stmtContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#function_stmt.
    def exitFunction_stmt(self, ctx:RParser.Function_stmtContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#if_stmt.
    def exitIf_stmt(self, ctx:RParser.If_stmtContext):
        ctx.text = child_catcher(ctx,'R',isCompStmt = True)


    # Exit a parse tree produced by RParser#for_stmt.
    def exitFor_stmt(self, ctx:RParser.For_stmtContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#while_stmt.
    def exitWhile_stmt(self, ctx:RParser.While_stmtContext):
        ctx.text = child_catcher(ctx,'R')


    # Enter a parse tree produced by RParser#suite.
    def enterSuite(self, ctx:RParser.SuiteContext):
        self.insuite = True
        if len(child_catcher(ctx,'R',list=True)) != 1:
            self.indent += 1


    # Exit a parse tree produced by RParser#suite.
    def exitSuite(self, ctx:RParser.SuiteContext):
        ctx.text = child_catcher(ctx,'R',isSuite=True,indent = self.indent)

        if len(child_catcher(ctx,'R',list=True)) != 1:
            self.indent -= 1

        if self.indent == 0:
            self.insuite = False


    # Exit a parse tree produced by RParser#simple_stmt.
    def exitSimple_stmt(self, ctx:RParser.Simple_stmtContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#help_stmt.
    def exitHelp_stmt(self, ctx:RParser.Help_stmtContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#kwrd_stmt.
    def exitKwrd_stmt(self, ctx:RParser.Kwrd_stmtContext):
        ctx.text = child_catcher(ctx,'R')


    # Enter a parse tree produced by RParser#assingment_stmt.
    def enterAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):
        self.atomcount = 0

    # Exit a parse tree produced by RParser#assingment_stmt.
    def exitAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):

        if self.atomcount == 2:

            children = child_catcher(ctx,'R',list = True)

            if children[0] in self.uncerts.keys():

                children[2] = self.uncerts[children[0]]

                ctx.text = ''

                for child in children:
                    ctx.text += child + ' '

                ctx.text += '\n'

            else: ctx.text = child_catcher(ctx,'R')


        else: ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#expr.
    def exitExpr(self, ctx:RParser.ExprContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#logical.
    def exitLogical(self, ctx:RParser.LogicalContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#arith.
    def exitArith(self, ctx:RParser.ArithContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#term.
    def exitTerm(self, ctx:RParser.TermContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#factor.
    def exitFactor(self, ctx:RParser.FactorContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#power.
    def exitPower(self, ctx:RParser.PowerContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#kwrd.
    def exitKwrd(self, ctx:RParser.KwrdContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#atom.
    def exitAtom(self, ctx:RParser.AtomContext):
        self.atomcount += 1
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#trailer.
    def exitTrailer(self, ctx:RParser.TrailerContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#formlist.
    def exitFormlist(self, ctx:RParser.FormlistContext):
        ctx.text = child_catcher(ctx,'R')



    # Exit a parse tree produced by RParser#form.
    def exitForm(self, ctx:RParser.FormContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#sublist.
    def exitSublist(self, ctx:RParser.SublistContext):
        ctx.text = child_catcher(ctx,'R')

    # Exit a parse tree produced by RParser#sub.
    def exitSub(self, ctx:RParser.SubContext):
        ctx.text = child_catcher(ctx,'R')


    # Exit a parse tree produced by RParser#assop.
    def exitAssop(self, ctx:RParser.AssopContext):
        ctx.text = child_catcher(ctx,'R')
