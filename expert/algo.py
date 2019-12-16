from classes import Data

def algo(data):

    # add first dapandencies from queries
    for query in data.listUnknownVars:
        if query in data.dictVarsStatuses and data.dictVarsStatuses[query] == 'False'
            listDependencies.append(str(query))
    
    # check if all vars we nedd is already known
    while not checkAllFound(data):
        # check first dependencies
        addDependencies(data)

        # find necessary rules
        
        # calculate all necesarry rules
        # output prev result
        # continue

def addDependencies(data):
    for rule in data.dictRules:

def checkAllFound(data):
    for elem in data.listUnknownVars:
        if elem in data.dictVarsStatuses.keys and data.dictVarsStatuses[elem] == False
            return 0
    return 1    

# add writing unexpected chars
# check if my parsing algo cannot add rubbish to my dictionaries
