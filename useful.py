import mpmath as mp

def has_child(ctx):
    if ctx.getChildCount() == 1:
        return True
    else:
        return False

def child_catcher(ctx, language ,list = False, space_needed = False, indent = 0, isSuite = False,
                  isCompStmt = False, tfpdef = False, import_from = False,noTerm = False):
    # Function to read text from all children of node of parse tree

    if language == 'Python3' or language == 'puffin':
        # Annoyingly when parsing antlr includes indents for only the first line of
        # suites in for/if etc statements, therefore they are manually added for each
        # line here

        if isSuite:
            # Adding new line at start of suite
            text = '\n'
        else:
            text = ''

        child_list = []

        # THIS IS TOO PYTHON SPECIFIC
        keywords = ['elif','else','except','finally']
        space_words = ['def','class','for','if','elif','from','with','lambda','try',
                        'async','global','nonlocal','assert','raise','return']
        super_space = ['as','and','or','not','in']

        if import_from:
            super_space.append('import')
        else:
            space_words.append('import')

        for child in ctx.children:

            if child.__class__.__name__ == 'TerminalNodeImpl':
                if isSuite or noTerm:

                    # Not including any whitespace or new line characters when reading suites
                    # Also not including «» symbols when reading elements from uq files
                    continue

                if isCompStmt and indent > 0:

                    if child.getText() in keywords:
                        text += '    '*indent+child.getText()
                        continue

                if not list:
                    if child.getText() in space_words:
                        text += child.getText()+' '
                        continue

                    elif child.getText() in super_space:
                        text += ' '+child.getText()+' '
                        continue

                    elif child.getText() == ':' and not tfpdef:
                        text += ':\n'
                        continue

            try:
                text += child.text
                child_list.append(child.text)
            except:
                text += child.getText()
                child_list.append(child.getText())

            # if (not text.endswith(' ') and
            #     not text.endswith(':') and
            #     not text.endswith('\n') and
            #     space_needed):
            #
            #     # Adding spaces when they are needed
            #     text += ' '

        # if isSuite:
        #     # Adding a new line at the end of suites
        #     text += '\n'

        if indent != 0 and not isCompStmt:
            # Adding the correct indentation when needed

            text = '    '*indent+text.strip()+'\n'


    elif language == 'R':

        child_list = []
        text = ''

        for child in ctx.children:

            try:

                child_text = child.text

            except:

                child_text = child.getText()
                # if isSuite:
                #     print(child.getText())



            child_list.append(child_text)

            if isSuite:

                if len(child_list) == 1:

                    if child_text == '{':
                        child_text += '\n'
                        child_text = ' ' + child_text

                if child_text == '}':
                    if indent != 0:
                        # Adding the correct indentation when needed
                        child_text = '    '*indent+child_text.strip()

            text += child_text


        if indent != 0 and not text.startswith(' {'):
            # Adding the correct indentation when needed

            text = '    '*indent+text.strip()+'\n'

        if isCompStmt and 'else' in text:
            text = text.replace('}else','} else')
    if list: return child_list
    else: return text


def checkLength(new,old):
    new = str(new)
    old = str(old)

    if '.' in new and '.' not in old and (len(new) > len(old) + 2):

        new = new[:len(old)+1]
    elif (len(new) > len(old) + 1):
        new = new[:len(old)]

    return new

def getSigFig(number):

    sNumber = str(number)
    if '.' in sNumber:
        int_,deci = sNumber.split('.')
        d = -len(deci)
    elif number == 0:
        d = 0
    else:
        zeros = '0'

        while sNumber.endswith(zeros):

            zeros += '0'

        d = len(zeros) - 1

    # d = len(str(number).replace('.',''))
    print(d)
    lower = number - 5*10**(d-1)
    higher = number + 5*10**(d-1)

    return lower,higher

def read_uncert(file):
    uncerts = {}
    with open(file,'r') as f:
        for line in f:
            if line.strip() != "":

                parts = [x.strip() for x in line.split('->')]
                uncerts[parts[0]] = parts[1]
    return uncerts
