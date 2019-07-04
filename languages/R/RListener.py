# Generated from R.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete listener for a parse tree produced by RParser.
class RListener(ParseTreeListener):

    # Enter a parse tree produced by RParser#file_input.
    def enterFile_input(self, ctx:RParser.File_inputContext):
        pass

    # Exit a parse tree produced by RParser#file_input.
    def exitFile_input(self, ctx:RParser.File_inputContext):
        pass


    # Enter a parse tree produced by RParser#stmt.
    def enterStmt(self, ctx:RParser.StmtContext):
        pass

    # Exit a parse tree produced by RParser#stmt.
    def exitStmt(self, ctx:RParser.StmtContext):
        pass


    # Enter a parse tree produced by RParser#complex_stmt.
    def enterComplex_stmt(self, ctx:RParser.Complex_stmtContext):
        pass

    # Exit a parse tree produced by RParser#complex_stmt.
    def exitComplex_stmt(self, ctx:RParser.Complex_stmtContext):
        pass


    # Enter a parse tree produced by RParser#simple_stmt.
    def enterSimple_stmt(self, ctx:RParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by RParser#simple_stmt.
    def exitSimple_stmt(self, ctx:RParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by RParser#expr.
    def enterExpr(self, ctx:RParser.ExprContext):
        pass

    # Exit a parse tree produced by RParser#expr.
    def exitExpr(self, ctx:RParser.ExprContext):
        pass


    # Enter a parse tree produced by RParser#assop.
    def enterAssop(self, ctx:RParser.AssopContext):
        pass

    # Exit a parse tree produced by RParser#assop.
    def exitAssop(self, ctx:RParser.AssopContext):
        pass


    # Enter a parse tree produced by RParser#arith.
    def enterArith(self, ctx:RParser.ArithContext):
        pass

    # Exit a parse tree produced by RParser#arith.
    def exitArith(self, ctx:RParser.ArithContext):
        pass


    # Enter a parse tree produced by RParser#term.
    def enterTerm(self, ctx:RParser.TermContext):
        pass

    # Exit a parse tree produced by RParser#term.
    def exitTerm(self, ctx:RParser.TermContext):
        pass


    # Enter a parse tree produced by RParser#factor.
    def enterFactor(self, ctx:RParser.FactorContext):
        pass

    # Exit a parse tree produced by RParser#factor.
    def exitFactor(self, ctx:RParser.FactorContext):
        pass


    # Enter a parse tree produced by RParser#power.
    def enterPower(self, ctx:RParser.PowerContext):
        pass

    # Exit a parse tree produced by RParser#power.
    def exitPower(self, ctx:RParser.PowerContext):
        pass


    # Enter a parse tree produced by RParser#element.
    def enterElement(self, ctx:RParser.ElementContext):
        pass

    # Exit a parse tree produced by RParser#element.
    def exitElement(self, ctx:RParser.ElementContext):
        pass


    # Enter a parse tree produced by RParser#id_name.
    def enterId_name(self, ctx:RParser.Id_nameContext):
        pass

    # Exit a parse tree produced by RParser#id_name.
    def exitId_name(self, ctx:RParser.Id_nameContext):
        pass


    # Enter a parse tree produced by RParser#atom.
    def enterAtom(self, ctx:RParser.AtomContext):
        pass

    # Exit a parse tree produced by RParser#atom.
    def exitAtom(self, ctx:RParser.AtomContext):
        pass


    # Enter a parse tree produced by RParser#suite.
    def enterSuite(self, ctx:RParser.SuiteContext):
        pass

    # Exit a parse tree produced by RParser#suite.
    def exitSuite(self, ctx:RParser.SuiteContext):
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


