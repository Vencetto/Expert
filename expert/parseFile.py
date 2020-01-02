from colorama import Fore, Style
import re

from constants import REGEXP_QUERIES, REGEXP_FACTS, REGEXP_ONE_RULE, OPS

def parseInput(fileInput, data):
    fault = False

    tempList = re.findall(REGEXP_ONE_RULE, fileInput, re.MULTILINE)
    for elem in tempList:
        data.allRules.append("".join(elem).strip())

    if len(data.allRules) == 0:
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
        getQueries(data)
        getKnownVars(data)


def getVariables(data):
    for rule in data.allRules:
        for char in rule:
            if char.isalpha() and char not in data.dictVarsStatuses:
                data.dictVarsStatuses[char] = False
            if not char.isalpha() and not char.isspace() and not char in OPS:
                data.listUnexpectedChars.append(char)

def getQueries(data):
    for querieChar in data.allQueries:
        if querieChar.isalpha() and querieChar not in data.listQueries:
            data.listQueries.append(querieChar)

def getKnownVars(data):
    for factChar in data.allFacts:
        if factChar.isalpha() and factChar in data.dictVarsStatuses:
            data.dictVarsStatuses[factChar] = True
