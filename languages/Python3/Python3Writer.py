from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

import sys
from useful import child_catcher

class Python3Writer(ParseTreeListener):

    def __init__(self, output,uncerts = {},translations = {},changes={}):
        self.output = output
        self.uncerts = uncerts
        self.changes = changes
        self.translations = translations
        self.output.write('import puffin\n')
        self.indent = 0


    def enterSuite(self, ctx:Python3Parser.SuiteContext):
        self.indent += 1

    ## Exit Functions
    def exitStmt(self, ctx:Python3Parser.StmtContext):

        if self.indent == 0:
            if ctx.getText().strip() in self.changes.keys():
                print(self.changes[ctx.getText().strip()])
                ctx.text = self.changes[ctx.getText().strip()]
            else:
                ctx.text = child_catcher(ctx,'Python3')
            self.output.write(ctx.text)
        else:
            ctx.text = child_catcher(ctx,'Python3',indent = self.indent)


    def exitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        ctx.text = child_catcher(ctx,'Python3',isCompStmt = True,indent = self.indent)


    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitSuite(self, ctx: Python3Parser.SuiteContext):
        ctx.text = child_catcher(ctx,'Python3', isSuite = True, indent = self.indent)
        self.indent -= 1

    def exitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitImport_stmt(self, ctx:Python3Parser.Import_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitImport_name(self, ctx:Python3Parser.Import_nameContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitImport_from(self, ctx:Python3Parser.Import_fromContext):
        ctx.text = child_catcher(ctx,'Python3',import_from = True)

    def exitImport_as_names(self, ctx:Python3Parser.Import_as_namesContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitImport_as_name(self, ctx:Python3Parser.Import_as_nameContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDotted_as_name(self, ctx:Python3Parser.Dotted_as_nameContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDotted_as_names(self, ctx:Python3Parser.Dotted_as_namesContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDotted_name(self, ctx:Python3Parser.Dotted_nameContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitArith_expr(self, ctx:Python3Parser.Arith_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitLambdef(self, ctx:Python3Parser.LambdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitExpr_stmt(self, ctx:Python3Parser.ExprlistContext):
        ctx.text = child_catcher(ctx,'Python3')

        for key in self.uncerts.keys():

            if ctx.text.startswith('%s=' %(key)):
                ctx.text = '%s=%s' %(key,self.uncerts[key])


    def exitTestlist_star_expr(self, ctx:Python3Parser.Testlist_star_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTest(self, ctx:Python3Parser.TestContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitOr_test(self, ctx:Python3Parser.Or_testContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAnd_test(self, ctx:Python3Parser.And_testContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitNot_test(self, ctx:Python3Parser.Not_testContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitComparison(self, ctx:Python3Parser.ComparisonContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitExpr(self, ctx:Python3Parser.ExprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitXor_expr(self, ctx:Python3Parser.Xor_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAnd_expr(self, ctx:Python3Parser.And_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitShift_expr(self, ctx:Python3Parser.Shift_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTerm(self, ctx:Python3Parser.TermContext):

        expr = child_catcher(ctx,'Python3')
        args = child_catcher(ctx,'Python3',list=True)

        ctx.text = expr

    def exitAtom_expr(self, ctx:Python3Parser.Atom_exprContext):
        ctx.text = child_catcher(ctx,'Python3')
        for key in self.translations.keys():
            if key in ctx.text:
                ctx.text = ctx.text.replace(key,self.translations[key])

    def exitPower(self, ctx:Python3Parser.PowerContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitFactor(self,ctx:Python3Parser.FactorContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAtom(self,ctx:Python3Parser.AtomContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDecorator(self, ctx:Python3Parser.DecoratorContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDecorators(self, ctx:Python3Parser.DecoratorsContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDecorated(self, ctx:Python3Parser.DecoratedContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAsync_funcdef(self, ctx:Python3Parser.Async_funcdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitParameters(self, ctx:Python3Parser.ParametersContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTypedargslist(self, ctx:Python3Parser.TypedargslistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTfpdef(self, ctx:Python3Parser.TfpdefContext):
        ctx.text = child_catcher(ctx,'Python3',tfpdef = True)

    def exitVarargslist(self, ctx:Python3Parser.VarargslistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitVfpdef(self, ctx:Python3Parser.VfpdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAnnassign(self, ctx:Python3Parser.AnnassignContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDel_stmt(self, ctx:Python3Parser.Del_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitPass_stmt(self, ctx:Python3Parser.Pass_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitYield_stmt(self, ctx:Python3Parser.Yield_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitRaise_stmt(self, ctx:Python3Parser.Raise_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitGlobal_stmt(self, ctx:Python3Parser.Global_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitNonlocal_stmt(self, ctx:Python3Parser.Nonlocal_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAssert_stmt(self, ctx:Python3Parser.Assert_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitAsync_stmt(self, ctx:Python3Parser.Async_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTry_stmt(self, ctx:Python3Parser.Try_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitExcept_clause(self, ctx:Python3Parser.Except_clauseContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitWith_stmt(self, ctx:Python3Parser.With_stmtContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitWith_item(self, ctx:Python3Parser.With_itemContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTest_nocond(self, ctx:Python3Parser.Test_nocondContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitLambdef_nocond(self, ctx:Python3Parser.Lambdef_nocondContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitComp_op(self, ctx:Python3Parser.Comp_opContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitStar_expr(self, ctx:Python3Parser.Star_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTrailer(self, ctx:Python3Parser.TrailerContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitSubscriptlist(self, ctx:Python3Parser.SubscriptlistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitSubscript(self, ctx:Python3Parser.SubscriptContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitSliceop(self, ctx:Python3Parser.SliceopContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitExprlist(self, ctx:Python3Parser.ExprlistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitTestlist(self, ctx:Python3Parser.TestlistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitDictorsetmaker(self, ctx:Python3Parser.DictorsetmakerContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitArglist(self, ctx:Python3Parser.ArglistContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitArgument(self, ctx:Python3Parser.ArgumentContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitComp_iter(self, ctx:Python3Parser.Comp_iterContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitComp_for(self, ctx:Python3Parser.Comp_forContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitComp_if(self, ctx:Python3Parser.Comp_ifContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitEncoding_decl(self, ctx:Python3Parser.Encoding_declContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitYield_expr(self, ctx:Python3Parser.Yield_exprContext):
        ctx.text = child_catcher(ctx,'Python3')

    def exitYield_arg(self, ctx:Python3Parser.Yield_argContext):
        ctx.text = child_catcher(ctx,'Python3')
