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
                ctx.text = child_catcher(ctx)
            self.output.write(ctx.text)
        else:
            ctx.text = child_catcher(ctx,indent = self.indent)


    def exitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        ctx.text = child_catcher(ctx,isCompStmt = True,indent = self.indent)


    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        ctx.text = child_catcher(ctx)

    def exitSuite(self, ctx: Python3Parser.SuiteContext):
        ctx.text = child_catcher(ctx, isSuite = True, indent = self.indent)
        self.indent -= 1

    def exitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitImport_stmt(self, ctx:Python3Parser.Import_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitImport_name(self, ctx:Python3Parser.Import_nameContext):
        ctx.text = child_catcher(ctx)

    def exitImport_from(self, ctx:Python3Parser.Import_fromContext):
        ctx.text = child_catcher(ctx,import_from = True)

    def exitImport_as_names(self, ctx:Python3Parser.Import_as_namesContext):
        ctx.text = child_catcher(ctx)

    def exitImport_as_name(self, ctx:Python3Parser.Import_as_nameContext):
        ctx.text = child_catcher(ctx)

    def exitDotted_as_name(self, ctx:Python3Parser.Dotted_as_nameContext):
        ctx.text = child_catcher(ctx)

    def exitDotted_as_names(self, ctx:Python3Parser.Dotted_as_namesContext):
        ctx.text = child_catcher(ctx)

    def exitDotted_name(self, ctx:Python3Parser.Dotted_nameContext):
        ctx.text = child_catcher(ctx)

    def exitArith_expr(self, ctx:Python3Parser.Arith_exprContext):
        ctx.text = child_catcher(ctx)

    def exitLambdef(self, ctx:Python3Parser.LambdefContext):
        ctx.text = child_catcher(ctx)

    def exitExpr_stmt(self, ctx:Python3Parser.ExprlistContext):
        ctx.text = child_catcher(ctx)

        for key in self.uncerts.keys():

            if ctx.text.startswith('%s=' %(key)):
                ctx.text = '%s=%s' %(key,self.uncerts[key])


    def exitTestlist_star_expr(self, ctx:Python3Parser.Testlist_star_exprContext):
        ctx.text = child_catcher(ctx)

    def exitTest(self, ctx:Python3Parser.TestContext):
        ctx.text = child_catcher(ctx)

    def exitOr_test(self, ctx:Python3Parser.Or_testContext):
        ctx.text = child_catcher(ctx)

    def exitAnd_test(self, ctx:Python3Parser.And_testContext):
        ctx.text = child_catcher(ctx)

    def exitNot_test(self, ctx:Python3Parser.Not_testContext):
        ctx.text = child_catcher(ctx)

    def exitComparison(self, ctx:Python3Parser.ComparisonContext):
        ctx.text = child_catcher(ctx)

    def exitExpr(self, ctx:Python3Parser.ExprContext):
        ctx.text = child_catcher(ctx)

    def exitXor_expr(self, ctx:Python3Parser.Xor_exprContext):
        ctx.text = child_catcher(ctx)

    def exitAnd_expr(self, ctx:Python3Parser.And_exprContext):
        ctx.text = child_catcher(ctx)

    def exitShift_expr(self, ctx:Python3Parser.Shift_exprContext):
        ctx.text = child_catcher(ctx)

    def exitTerm(self, ctx:Python3Parser.TermContext):

        expr = child_catcher(ctx)
        args = child_catcher(ctx,list=True)

        ctx.text = expr

    def exitAtom_expr(self, ctx:Python3Parser.Atom_exprContext):
        ctx.text = child_catcher(ctx)
        for key in self.translations.keys():
            if key in ctx.text:
                ctx.text = ctx.text.replace(key,self.translations[key])

    def exitPower(self, ctx:Python3Parser.PowerContext):
        ctx.text = child_catcher(ctx)

    def exitFactor(self,ctx:Python3Parser.FactorContext):
        ctx.text = child_catcher(ctx)

    def exitAtom(self,ctx:Python3Parser.AtomContext):
        ctx.text = child_catcher(ctx)

    def exitDecorator(self, ctx:Python3Parser.DecoratorContext):
        ctx.text = child_catcher(ctx)

    def exitDecorators(self, ctx:Python3Parser.DecoratorsContext):
        ctx.text = child_catcher(ctx)

    def exitDecorated(self, ctx:Python3Parser.DecoratedContext):
        ctx.text = child_catcher(ctx)

    def exitAsync_funcdef(self, ctx:Python3Parser.Async_funcdefContext):
        ctx.text = child_catcher(ctx)

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        ctx.text = child_catcher(ctx)

    def exitParameters(self, ctx:Python3Parser.ParametersContext):
        ctx.text = child_catcher(ctx)

    def exitTypedargslist(self, ctx:Python3Parser.TypedargslistContext):
        ctx.text = child_catcher(ctx)

    def exitTfpdef(self, ctx:Python3Parser.TfpdefContext):
        ctx.text = child_catcher(ctx,tfpdef = True)

    def exitVarargslist(self, ctx:Python3Parser.VarargslistContext):
        ctx.text = child_catcher(ctx)

    def exitVfpdef(self, ctx:Python3Parser.VfpdefContext):
        ctx.text = child_catcher(ctx)

    def exitAnnassign(self, ctx:Python3Parser.AnnassignContext):
        ctx.text = child_catcher(ctx)

    def exitDel_stmt(self, ctx:Python3Parser.Del_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitPass_stmt(self, ctx:Python3Parser.Pass_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitYield_stmt(self, ctx:Python3Parser.Yield_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitRaise_stmt(self, ctx:Python3Parser.Raise_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitGlobal_stmt(self, ctx:Python3Parser.Global_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitNonlocal_stmt(self, ctx:Python3Parser.Nonlocal_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitAssert_stmt(self, ctx:Python3Parser.Assert_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitAsync_stmt(self, ctx:Python3Parser.Async_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitTry_stmt(self, ctx:Python3Parser.Try_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitExcept_clause(self, ctx:Python3Parser.Except_clauseContext):
        ctx.text = child_catcher(ctx)

    def exitWith_stmt(self, ctx:Python3Parser.With_stmtContext):
        ctx.text = child_catcher(ctx)

    def exitWith_item(self, ctx:Python3Parser.With_itemContext):
        ctx.text = child_catcher(ctx)

    def exitTest_nocond(self, ctx:Python3Parser.Test_nocondContext):
        ctx.text = child_catcher(ctx)

    def exitLambdef_nocond(self, ctx:Python3Parser.Lambdef_nocondContext):
        ctx.text = child_catcher(ctx)

    def exitComp_op(self, ctx:Python3Parser.Comp_opContext):
        ctx.text = child_catcher(ctx)

    def exitStar_expr(self, ctx:Python3Parser.Star_exprContext):
        ctx.text = child_catcher(ctx)

    def exitTrailer(self, ctx:Python3Parser.TrailerContext):
        ctx.text = child_catcher(ctx)

    def exitSubscriptlist(self, ctx:Python3Parser.SubscriptlistContext):
        ctx.text = child_catcher(ctx)

    def exitSubscript(self, ctx:Python3Parser.SubscriptContext):
        ctx.text = child_catcher(ctx)

    def exitSliceop(self, ctx:Python3Parser.SliceopContext):
        ctx.text = child_catcher(ctx)

    def exitExprlist(self, ctx:Python3Parser.ExprlistContext):
        ctx.text = child_catcher(ctx)

    def exitTestlist(self, ctx:Python3Parser.TestlistContext):
        ctx.text = child_catcher(ctx)

    def exitDictorsetmaker(self, ctx:Python3Parser.DictorsetmakerContext):
        ctx.text = child_catcher(ctx)

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        ctx.text = child_catcher(ctx)

    def exitArglist(self, ctx:Python3Parser.ArglistContext):
        ctx.text = child_catcher(ctx)

    def exitArgument(self, ctx:Python3Parser.ArgumentContext):
        ctx.text = child_catcher(ctx)

    def exitComp_iter(self, ctx:Python3Parser.Comp_iterContext):
        ctx.text = child_catcher(ctx)

    def exitComp_for(self, ctx:Python3Parser.Comp_forContext):
        ctx.text = child_catcher(ctx)

    def exitComp_if(self, ctx:Python3Parser.Comp_ifContext):
        ctx.text = child_catcher(ctx)

    def exitEncoding_decl(self, ctx:Python3Parser.Encoding_declContext):
        ctx.text = child_catcher(ctx)

    def exitYield_expr(self, ctx:Python3Parser.Yield_exprContext):
        ctx.text = child_catcher(ctx)

    def exitYield_arg(self, ctx:Python3Parser.Yield_argContext):
        ctx.text = child_catcher(ctx)
