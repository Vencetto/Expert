from colorama import Fore, Style
import re

REGEXP_RULES = "\n|^([\w\s]*[\W\S]*)\n?"
REGEXP_ONE_RULE = "^([\(\)\|\^\w\s\+\!\-]+)(=>|<=>)([\(\)\|\^\w\s\+\!\-]+)(#|\n)"
REGEXP_FACTS = "(\=\w+)"
REGEXP_QUERIES = "(\?\w+)"

def parseInput(fileInput, data):
    fault = False
    
    rules = re.search(REGEXP_RULES, fileInput)
    if not rules:
        print(Fore.YELLOW + "rules was not found in file")
        fault = True
        
    facts = re.search(REGEXP_FACTS, fileInput)
    if not facts:
        print(Fore.YELLOW + "facts was not found in file")
        fault = True
        
    queries = re.search(REGEXP_QUERIES, fileInput)
    if not queries:
        print(Fore.YELLOW + "queries was not found in file")
        fault = True

    if fault:
        print(Fore.RED + "Input file component not found")
        return ;

   # data.allRules = getRules(rules)
#    data.allFacts = getFacts(facts)
 #   data.allQueries = getQueries(queries)
    
#def getRules(stringWithRules):
    
