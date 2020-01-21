# Generated from R.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

import sys
from useful import child_catcher, has_child

# This class defines a complete listener for a parse tree produced by RParser.
class RReader(ParseTreeListener):

    def __init__(self, output):
        self.output = output
        self.vardec = False
        self.list_text = ""
        self.funname = ""
        self.repvar = {}


    # Exit a parse tree produced by RParser#stmt.
    def exitStmt(self, ctx:RParser.StmtContext):

        if self.vardec:
            if self.list_text != "":

                text = ctx.getText().split('=')[0]+' -> '+self.list_text +'\n'
            else:

                text = child_catcher(ctx,'R',space_needed = True)+'\n'

            if self.funname != "":

                text = "%s.%s" %(self.funname,text)

            varname = text.split('->')[0].strip()
            if varname not in self.repvar.keys():
                self.repvar[varname] = 1
            else:
                self.repvar[varname] += 1
                text = text.replace(varname,"%s!%i" %(varname,self.repvar[varname]))

            self.output.write(text)

    # Exit a parse tree produced by RParser#simple_stmt.
    def exitSimple_stmt(self, ctx:RParser.Simple_stmtContext):
        if self.vardec:
            ctx.text = child_catcher(ctx,'R')

    # Enter a parse tree produced by RParser#function_stmt.
    def enterFunction_stmt(self, ctx:RParser.Function_stmtContext):
        self.funname = child_catcher(ctx,'R',list = True)[0]


    # Exit a parse tree produced by RParser#function_stmt.
    def exitFunction_stmt(self, ctx:RParser.Function_stmtContext):
        self.funname = ""
        self.vardec = False

    # Enter a parse tree produced by RParser#assingment_stmt.
    def enterAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):
        if ctx.getChildCount() == 3:
            self.vardec = True
        else:
            self.vardec = False

    # Exit a parse tree produced by RParser#assingment_stmt.
    def exitAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):
        if self.vardec:
            ctx.text = child_catcher(ctx,'R')

    # Enter a parse tree produced by RParser#expr.
    def enterExpr(self, ctx:RParser.ExprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    # Enter a parse tree produced by RParser#logical.
    def enterLogical(self, ctx:RParser.LogicalContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    # Enter a parse tree produced by RParser#arith.
    def enterArith(self, ctx:RParser.ArithContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    # Enter a parse tree produced by RParser#term.
    def enterTerm(self, ctx:RParser.TermContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Enter a parse tree produced by RParser#factor.
    def enterFactor(self, ctx:RParser.FactorContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    # Enter a parse tree produced by RParser#power.
    def enterPower(self, ctx:RParser.PowerContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Enter a parse tree produced by RParser#kwrd.
    def enterKwrd(self, ctx:RParser.KwrdContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    # Enter a parse tree produced by RParser#atom.
    def enterAtom(self, ctx:RParser.AtomContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Enter a parse tree produced by RParser#assop.
    def enterAssop(self, ctx:RParser.AssopContext):
        ctx.text = ' -> '
