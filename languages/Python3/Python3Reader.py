from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

import sys
from useful import has_child, child_catcher

class Python3Reader(ParseTreeListener):

    def __init__(self, output):
        self.output = output
        self.vardec = False
        self.list_text = ""
        self.funname = ""
        self.repvar = {}


    ## Functions that do things
    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        self.funname = child_catcher(ctx,'Python3',list=True)[1]
    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        self.funname = ""


    def enterExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):
        self.list_text = ""
        if ctx.getChildCount() == 3:
            self.vardec = True
        else:
            self.vardec = False

    def enterAtom(self, ctx:Python3Parser.AtomContext):
        for child in ctx.getChildren():
            if child.__class__.__name__ == 'Testlist_compContext':
                if ctx.getText().startswith('('):
                    self.list_text = 'touple' + ctx.getText()
                else:
                    self.list_text = ctx.getText().replace('[','list(').replace(']',')')

        if ctx.getText() == '[]':
            self.list_text = 'list()'

    def exitExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):
        if self.vardec:
            if self.list_text != "":


                text = ctx.getText().split('=')[0]+' -> '+self.list_text +'\n'
            else:

                text = ctx.getText().replace('=',' -> ')+'\n'

            if self.funname != "":

                text = "%s.%s" %(self.funname,text)


            varname = text.split('->')[0].strip()
            if varname not in self.repvar.keys():
                self.repvar[varname] = 1
            else:
                self.repvar[varname] += 1
                text = text.replace(varname,"%s!%i" %(varname,self.repvar[varname]))


            self.output.write(text)


    # Fodder funcitons
    def enterTestlist_star_expr(self,ctx:Python3Parser.Testlist_star_exprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterTest(self,ctx:Python3Parser.TestContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterOr_test(self,ctx:Python3Parser.Or_testContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterAnd_test(self,ctx:Python3Parser.And_testContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterNot_test(self,ctx:Python3Parser.Not_testContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterComparison(self,ctx:Python3Parser.ComparisonContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterExpr(self,ctx:Python3Parser.ExprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterXor_expr(self,ctx:Python3Parser.Xor_exprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterAnd_expr(self,ctx:Python3Parser.And_exprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterShift_expr(self,ctx:Python3Parser.Shift_exprContext):

        if self.vardec:
            self.vardec = has_child(ctx)

    def enterArith_expr(self, ctx:Python3Parser.Arith_exprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterTerm(self,ctx:Python3Parser.TermContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterFactor(self,ctx:Python3Parser.FactorContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterPower(self,ctx:Python3Parser.PowerContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterAtom_expr(self, ctx:Python3Parser.Atom_exprContext):
        if self.vardec:
            self.vardec = has_child(ctx)

    def enterAugassign(self,ctx:Python3Parser.AugassignContext):
        #  a += 1 etc
        self.vardec = False
