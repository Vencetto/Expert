from colorama import Fore, Style
import re

REGEXP_ONE_RULE = r'^(\!?[A-Z][A-Z\s\|\+\(\)\!\^]*)(=>|<=>)(\s*\!?[A-Z][A-Z\s\|\+\(\)\!\^]*)[\#|\n]'
REGEXP_FACTS = r'(\=\w+)'
REGEXP_QUERIES = r'(\?\w+)'

def parseInput(fileInput, data):
    fault = False

    tempList = re.findall(REGEXP_ONE_RULE, fileInput, re.MULTILINE)
    for elem in tempList:
        data.dictRules["".join(elem).strip()] = elem

    if len(data.dictRules) == 0:
        print(Fore.YELLOW + "Rules was not found in file")
        fault = True
        
    facts = re.search(REGEXP_FACTS, fileInput)
    if not facts:
        print(Fore.YELLOW + "Facts was not found in file")
        fault = True
    else:
        data.allFacts = str(facts.group(0))

    queries = re.search(REGEXP_QUERIES, fileInput)
    if not queries:
        print(Fore.YELLOW + "Queries was not found in file")
        fault = True
    else:
        data.allQueries = str(queries.group(0))

    if fault:
        print(Fore.RED + "Input file component not found")
        return ;
    else:
        getVariables(data)
        getUnknownVars(data)
        getKnownVars(data)


def getVariables(data):
    for rule in data.dictRules:
        for char in rule:
            if char.isalpha() and char not in data.dictVarsStatuses:
                data.dictVarsStatuses[char] = False
            if not char.isalpha():
                data.listOfUnexpectedChars.append(char)
                

def getUnknownVars(data):
    for querieChar in data.allQueries:
        if querieChar.isalpha() and querieChar not in data.listUnknownVars:
            data.listUnknownVars.append(querieChar)

def getKnownVars(data):
    for factChar in data.allFacts:
        if factChar.isalpha() and factChar in data.dictVarsStatuses:
            data.dictVarsStatuses[factChar] = True
