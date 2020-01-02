from classes import Data

def algo(data):

    # add first dapandencies from queries
    for queryLetter in data.listQueries:
        if queryLetter in data.dictVarsStatuses and data.dictVarsStatuses[queryLetter] == 'False' and not queryLetter in data.listDependencies:
            data.stackDependencies.append(str(queryLetter))
            print('{queryLetter} added to stack of dependencies')
    
    # check if all vars we need is already known
    while len(data.stackDependencies) > 0:
        
        # go though every rule and find those letters which need to be found
        for rule in data.allRules:

            # check vars in rule to be dependent / needed to be find / are in list listUnknownVars
            if checkDependencies(rule.split('=>')[-1], data.listUnknownVars): # get right part of sentence, after '=>'

                # if all vars are known and operations are expected
                if checkCanCalculate(rule.replace(' ', ''), data):

                    # calculate rule and write vars
                    
                    # print previous result
                    printPrevResult()
                else:
                    # go to next rule
                    continue

def checkDependencies(rule, listUnknownVars):
    # check if in rule exists one of the wanted vars
    if any(unknown in rule in listQueries): # this is not robust, check it later

        # DELETE NEXT ROW LATER
        print(f'found one of the list {0} in {rule}'.format(', '.join(lisQueries)))

        return 1
    else:
        return 0
'''

resolve query:
    lookup among atomic
    if found
        return
    else
        push query
        resolve among complex
        pop query

resolve among complex:
    find all propositions with query as a part of rhs
    for query in found
        result <- solve lhs
        if result is undetermined
            undetermined
        if implication
            if result is true
                solve rhs as true
            else
                undetermined
        else if iff
            solve rhs as result


solve rhs as result:
    if result if undetermined
        undetermined
    if rhs is atomic
        result
    if rhs operation is NOT
        not result
    if binary operation (a,b):
        let second = if fact == a then b else a 
        if OR and result is false
            false
        if OR and result is true
            if second is false
                true
            else
                undetermined
        if AND and result is true
            true
        if AND and result is false
            if second is true
                false
            else
                undetermined
        if XOR and result is false
            return second
        if XOR and result is true
            not second

'''
