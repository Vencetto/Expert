from classes import Data

OPERATIONS = '+!|^()=<>'

def algo(data):

    # add first dapandencies from queries
    for queryLetter in data.listUnknownVars:
        if queryLetter in data.dictVarsStatuses and data.dictVarsStatuses[queryLetter] == 'False' and not queryLetter in data.listDependencies
            data.listDependencies.append(str(queryLetter))
            print('{query} added to list of dependencies')
    
    # check if all vars we nedd is already known
    while not checkAllFound(data):
        
        # go though every rule and find those letters which need to be found
        for rule in data.dictRules:

            # check vars in rule to be dependent / needed to be find / are in list listUnknownVars
            if checkDependencies(rule, data.listUnknownVars):

                # if all vars are known and operations are expected
                if checkCanCalculate(rule.replace(' ', ''), data):

                    # calculate rule and write vars
                    if not calculate(rule, data):
                        return 0
                    # print previous result
                    printPrevResult()
                else:
                    # go to next rule
                    continue

def calculate(rule, data): # maybe should try replacing calculated part with 1 or 0 OR replacing all vars with them idk...
    print('calculating {rule}')
    i = 0

    for char in rule:
        if char.isalpha():
            continue # maybe return it's value somehow
        elif char in OPERATIONS: # more functionality, more if'es
            if char == '(' or char == ')':
               if checkBrackets(rule):
                   calculate(rule[i + 1: rule.rfind(')') - 1]) # find last bracket, them feed this str[i:] to calculate func
                else:
                    return ''
            if char == '=' and rule[i + 1] == '>':
                # => case
            if if char == '<' and (len(rule) > i + 1) and rule[i + 1] == '=' and rule[i + 2] == '>':
                # case <=>
            if len(rule[:i]) == 1 and len(rule[i:]) == 1 # this won't work 
                basicOp(data.dictVarsStatuses[rule[:i]], data.dictVarsStatuses[rule[i:]], char)
        else:
            calculate(rule[i:], data)
        i += 1

def checkBrackets(rule): 
    open_br = '(' 
    close_br = ')'
    map = dict(zip(open_br, close_br)) 
    queue = []
  
    for i in rule: 
        if i in open_br: 
            queue.append(map[i]) 
        elif i in close_br: 
            if not queue or i != queue.pop(): 
                return 0
    return 1

def basicOp(v1, v2, op):
    if op == '+':
        return bool(v1) and bool(v2)
    elif op == '|':
        return bool(v1) or bool(v2)
    elif op == '!':
        return not bool(v2)
    elif op == '^':
        return bool(v1) != bool(v2)


def checkCanCalculate(rule, data):
    for char in rule:
        if char.isspace():
            continue
        elif char in OPERATIONS:
            continue
        elif char.isalpha():
            continue
        elif char in data.listDependencies:
            return 0
        else:
            return 0
    print("{rule} can be calculated")
    return 1

def checkDependencies(rule, listUnknownVars):
    # check if in rule exists one of the wanted vars
    if any(unknown in rule in listUnknownVars):

        # DELETE NEXT ROW LATER
        print(f'found one of the list {0} in {rule}'.format(', '.join(listUnknownVars)))

        return 1
    else:
        return 0

def checkAllFound(data):
    for elem in data.listUnknownVars:
        # if element exist is dictionary of vars and it is 'False' -> not everything found
        if elem in data.dictVarsStatuses.keys and data.dictVarsStatuses[elem] == False
            return 0
    return 1    
