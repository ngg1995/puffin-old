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


    # Exit a parse tree produced by RParser#stmt.
    def exitStmt(self, ctx:RParser.StmtContext):


        if self.vardec:
            if self.list_text != "":

                text = ctx.getText().split('=')[0]+' -> '+self.list_text +'\n'
            else:

                text = ctx.getText()+'\n'
                print(child_catcher(ctx))

            if self.funname != "":

                text = "%s.%s" %(self.funname,text)

            self.output.write(text)


    # Exit a parse tree produced by RParser#simple_stmt.
    def exitSimple_stmt(self, ctx:RParser.Simple_stmtContext):
        if self.vardec:
            ctx.text = child_catcher(ctx)

    # Enter a parse tree produced by RParser#function_stmt.
    def enterFunction_stmt(self, ctx:RParser.Function_stmtContext):
        self.funname = child_catcher(ctx,list = True)[2]


    # Exit a parse tree produced by RParser#function_stmt.
    def exitFunction_stmt(self, ctx:RParser.Function_stmtContext):
        self.funname = ""

    # Enter a parse tree produced by RParser#assingment_stmt.
    def enterAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):
        if ctx.getChildCount() == 3:
            self.vardec = True
        else:
            self.vardec = False


    # Exit a parse tree produced by RParser#assingment_stmt.
    def exitAssingment_stmt(self, ctx:RParser.Assingment_stmtContext):
        if self.vardec:
            ctx.text = child_catcher(ctx)

    # Enter a parse tree produced by RParser#expr.
    def enterExpr(self, ctx:RParser.ExprContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#expr.
    def exitExpr(self, ctx:RParser.ExprContext):
        pass


    # Enter a parse tree produced by RParser#logical.
    def enterLogical(self, ctx:RParser.LogicalContext):
        if self.vardec:
            self.vardec = has_child(ctx)



    # Exit a parse tree produced by RParser#logical.
    def exitLogical(self, ctx:RParser.LogicalContext):
        pass


    # Enter a parse tree produced by RParser#arith.
    def enterArith(self, ctx:RParser.ArithContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#arith.
    def exitArith(self, ctx:RParser.ArithContext):
        pass


    # Enter a parse tree produced by RParser#term.
    def enterTerm(self, ctx:RParser.TermContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#term.
    def exitTerm(self, ctx:RParser.TermContext):
        pass


    # Enter a parse tree produced by RParser#factor.
    def enterFactor(self, ctx:RParser.FactorContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#factor.
    def exitFactor(self, ctx:RParser.FactorContext):
        pass


    # Enter a parse tree produced by RParser#power.
    def enterPower(self, ctx:RParser.PowerContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#power.
    def exitPower(self, ctx:RParser.PowerContext):
        pass


    # Enter a parse tree produced by RParser#kwrd.
    def enterKwrd(self, ctx:RParser.KwrdContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#kwrd.
    def exitKwrd(self, ctx:RParser.KwrdContext):
        pass


    # Enter a parse tree produced by RParser#atom.
    def enterAtom(self, ctx:RParser.AtomContext):
        if self.vardec:
            self.vardec = has_child(ctx)


    # Exit a parse tree produced by RParser#atom.
    def exitAtom(self, ctx:RParser.AtomContext):
        pass


    # Enter a parse tree produced by RParser#trailer.
    def enterTrailer(self, ctx:RParser.TrailerContext):
        pass

    # Exit a parse tree produced by RParser#trailer.
    def exitTrailer(self, ctx:RParser.TrailerContext):
        pass


    # Enter a parse tree produced by RParser#formlist.
    def enterFormlist(self, ctx:RParser.FormlistContext):
        pass

    # Exit a parse tree produced by RParser#formlist.
    def exitFormlist(self, ctx:RParser.FormlistContext):
        pass


    # Enter a parse tree produced by RParser#form.
    def enterForm(self, ctx:RParser.FormContext):
        pass

    # Exit a parse tree produced by RParser#form.
    def exitForm(self, ctx:RParser.FormContext):
        pass


    # Enter a parse tree produced by RParser#sublist.
    def enterSublist(self, ctx:RParser.SublistContext):
        pass

    # Exit a parse tree produced by RParser#sublist.
    def exitSublist(self, ctx:RParser.SublistContext):
        pass


    # Enter a parse tree produced by RParser#sub.
    def enterSub(self, ctx:RParser.SubContext):
        pass

    # Exit a parse tree produced by RParser#sub.
    def exitSub(self, ctx:RParser.SubContext):
        pass


    # Enter a parse tree produced by RParser#assop.
    def enterAssop(self, ctx:RParser.AssopContext):
        ctx.text = '->'

    # Exit a parse tree produced by RParser#assop.
    def exitAssop(self, ctx:RParser.AssopContext):
        ctx.text = ' -> '
