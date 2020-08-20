from antlr4 import *
if __name__ is not None and "." in __name__:
    from .puffinParser import puffinParser
else:
    from puffinParser import puffinParser


import sys
from useful import child_catcher
import mpmath as mp
import pandas as pd

sigfigs = lambda x: len(str(x).replace('.',''))
getNumber = lambda n, ctx: child_catcher(ctx,'puffin',list=True)[n]

# This class defines a complete listener for a parse tree produced by puffinParser.
class puffinListener(ParseTreeListener):

    def __init__(self,target,dependencies = pd.DataFrame()):

        self.target = target
        self.dependencies = dependencies
        self.uncerts = {}
        self.changes = {}
        self.directChange = False


    # Exit a parse tree produced by puffinParser#file_input.
    def exitFile_input(self, ctx:puffinParser.File_inputContext):
        for line in child_catcher(ctx,'puffin',list=True,noTerm = True):
            if line.strip() != "":
                parts = [x.strip() for x in line.split('->')]
                # print(line)
                if '«' in line:

                    self.changes[parts[0].replace("«",'').replace("»","")] = parts[1]

                else:

                    if parts[0] in self.uncerts.keys():

                        print("%s has been reassinged multiple times. Only the last entry will be used" %(parts[0]))

                    # print(parts)
                    self.uncerts[parts[0]] = parts[1]

    # Exit a parse tree produced by puffinParser#assignment.
    def exitAssignment(self, ctx:puffinParser.AssignmentContext):

        ctx.text = child_catcher(ctx,'puffin')

    def enterAssignment(self, ctx:puffinParser.AssignmentContext):
        childtypes = [x.__class__.__name__ for x in ctx.children]
        if childtypes[0] == 'ElementContext':
            self.directChange = True


    # Exit a parse tree produced by puffinParser#collection.
    def exitCollection(self, ctx:puffinParser.CollectionContext):
        ctx.text = child_catcher(ctx,'puffin')


    # Exit a parse tree produced by puffinParser#atom.
    def exitAtom(self, ctx:puffinParser.AtomContext):
        ctx.text = child_catcher(ctx,'puffin')


    # Exit a parse tree produced by puffinParser#interval.
    def exitInterval(self, ctx:puffinParser.IntervalContext):
        if self.target == 'Python3':
            ctx.text = child_catcher(ctx,'puffin').replace('[','puffin.I(').replace(']',')')
        if self.target == 'R':
            ctx.text = child_catcher(ctx,'puffin').replace('[','interval(').replace(']',')')


    # Exit a parse tree produced by puffinParser#interval_basic.
    def exitInterval_basic(self, ctx:puffinParser.Interval_basicContext):
        ctx.text = child_catcher(ctx,'puffin')


    # Exit a parse tree produced by puffinParser#interval_plusminus.
    def exitInterval_plusminus(self, ctx:puffinParser.Interval_plusminusContext):
        asList = child_catcher(ctx,'puffin', list = True)
        a = mp.mpf(asList[1])
        b = mp.mpf(asList[3])

        ctx.text = '[%s,%s]' %(a-b,a+b)


    # Exit a parse tree produced by puffinParser#interval_pct.
    def exitInterval_pct(self, ctx:puffinParser.Interval_pctContext):
        asList = child_catcher(ctx,'puffin', list = True)
        a = mp.mpf(asList[1])
        b = mp.mpf(asList[3])/100

        ctx.text = '[%s,%s]' %(a*(1+b),a*(1-b))


    # Exit a parse tree produced by puffinParser#list_stmt.
    def exitList_stmt(self, ctx:puffinParser.List_stmtContext):
        if self.target == 'Python3':

            ctx.text = ctx.getText().replace('list(','[').replace(')',']')

        elif self.target == 'R':

            ctx.text = ctx.getText().replace('list(','c(')



    # Exit a parse tree produced by puffinParser#touple_stmt.
    def exitTouple_stmt(self, ctx:puffinParser.Touple_stmtContext):
        if self.target == 'Python3':

            ctx.text = ctx.getText().replace('touple','')

        elif self.target == 'R':

            ctx.text = ctx.getText().replace('touple','c')


    # Exit a parse tree produced by puffinParser#id_name.
    def exitId_name(self, ctx:puffinParser.Id_nameContext):
        pass


    # Exit a parse tree produced by puffinParser#pct.
    def exitPct(self, ctx:puffinParser.PctContext):

        ctx.text = ctx.getText().replace('%','')


    def exitElement(self, ctx:puffinParser.ElementContext):
        ctx.text = child_catcher(ctx,'puffin')

        if not self.directChange:
            if '<<' in ctx.text:
                ctx.text = ctx.text.replace('<<','').replace('>>','')
            else:
                ctx.text = ctx.text.replace('«','').replace('»','')
        else:
            ctx.text = ctx.text.replace('<<','«').replace('>>','»')
            self.directChange = False


    def exitPdistribution(self, ctx:puffinParser.PdistributionContext):

        asList = child_catcher(ctx,'puffin',list = True)

        if self.target == 'Python3':

            asList[0] = 'puffin.' + asList[0]

        elif self.target == 'R':

            pass # No syntax change

        ctx.text = ''
        for i in asList: ctx.text += i



    # Exit a parse tree produced by puffinParser#about.
    def exitAbout(self, ctx:puffinParser.AboutContext):
        # Statement is of form x -> about 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - 2*10**(-d)
        higher = n + 2*10**(-d)

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)

    # Exit a parse tree produced by puffinParser#Around.
    def exitAround(self, ctx:puffinParser.AroundContext):
        # Statement is of form x -> around 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - 10*10**(-d)
        higher = n + 10*10**(-d)

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#count.
    def exitCount(self, ctx:puffinParser.CountContext):
        # Statement is of form x -> count 10
        import math

        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - math.sqrt(n)
        higher = n + math.sqrt(n)

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#Over.
    def exitOver(self, ctx:puffinParser.OverContext):
        # Statement is of form x -> over 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n
        higher = n + 0.5+10**(-d)

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    def exitAlmost(self, ctx:puffinParser.AlmostContext):
        # Statement is of form x -> over 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - 0.5+10**(-d)
        higher = n

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#Over.
    def exitBelow(self, ctx:puffinParser.BelowContext):
        # Statement is of form x -> below 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - 0.5*10**(-d)
        higher = n

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#exitAbove.
    def exitAbove(self, ctx:puffinParser.AboveContext):
        # Statement is of form x -> above 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n - 0.5*10**(-d)
        higher = n

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#At_most.
    def exitAt_most(self, ctx:puffinParser.At_mostContext):
        # Statement is of form x -> at most 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        if n > 0:

            lower = 0
        else:
            lower = 'puffin.ninf'

        higher = n

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#At_least.
    def exitAt_least(self, ctx:puffinParser.At_mostContext):
        # Statement is of form x -> at least 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        lower = n

        higher = 'puffin.inf'

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    # Exit a parse tree produced by puffinParser#At_least.
    def exitOrder(self, ctx:puffinParser.OrderContext):
        # Statement is of form x -> order 10
        x = getNumber(1,ctx)
        n = mp.mpf(x)

        d = sigfigs(x)

        lower = n/2

        higher = 5*n

        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)


    def exitBetween(self, ctx:puffinParser.BetweenContext):

        lower = getNumber(1,ctx)
        higher = getNumber(3,ctx)


        if self.target == 'Python3':

            ctx.text = 'puffin.I(%s,%s)' %(lower,higher)

        elif self.target == 'R':

            ctx.text = 'interval(%s,%s)' %(lower,higher)

    # Enter a parse tree produced by puffinParser#dependence.
    def enterDependence(self, ctx:puffinParser.DependenceContext):

        # detect dependancies

        # puffin format will is as follows:
        # a <fiop> b,c,d,....

        # will be stored in a dataframe

        children = child_catcher(ctx,'puffin',list=True,noTerm = True)

        named = children.pop(0)

        deptype = children.pop(0).replace('<','').replace('>','')

        for child in children:


            # check to see if dependence already specified
            if named in self.dependencies.index and child in self.dependencies.index:
                # check if dependencies clash
                if deptype != 'f' and self.dependencies.loc[named,child] == 'f':
                    # this is allowed
                    pass
                elif deptype == self.dependencies.loc[named,child]:
                    # this is allowed
                    pass
                else:
                    raise Exception('Stated Dependancies Clash')

            else:
                # if not specided specify them
                if named not in self.dependencies.index:
                    self.dependencies.loc[named,named] = 'p'
                if child not in self.dependencies.index:
                    self.dependencies.loc[child,child] = 'p'

            self.dependencies.loc[named,child] = deptype
            self.dependencies.loc[child,named] = deptype

            self.dependencies = self.dependencies.fillna('f')


    # Exit a parse tree produced by puffinParser#dependence.
    def exitDependence(self, ctx:puffinParser.DependenceContext):
        ctx.text = '' # dont want to print out in new file
