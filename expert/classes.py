from colorama import Fore
from collections import deque

class Data:
    allFacts = ""               # string with input facts
    allQueries = ""             # string with input queries
    allRules = []               # list of input rules
    dictVarsStatuses = {}       # dictionary (var, like 'A' - status, like 'True')
    listQueries = []            # list of vars to find - ?ABC, queries
    stackDependencies = deque() # deque of dependencies for algorithm, what we nned to find to get final answer
    listUnexpectedChars = []    # list of chars, that we do not expect to apper in constructions or couldn't recognise

    def showFacts(self):
        print(Fore.CYAN + "This was recognised as facts -> " + Fore.WHITE + self.allFacts)

    def showQueries(self):
        print(Fore.CYAN + "This was recognised as queries -> " + Fore.WHITE + self.allQueries)

    def showEveryRule(self):
        if len(self.allRules) == 0:
            print(Fore.RED + "No rules were recognised")
            return
        for rule in self.allRules:
            print(Fore.YELLOW + "This was recognised as rule -> " + Fore.WHITE + rule)

    def showVarsStatuses(self):
        if len(self.dictVarsStatuses) == 0:
            print(Fore.RED + "No vars were recognised.")
            return

        print(Fore.GREEN + "True are ", end = '')
        for key in sorted(self.dictVarsStatuses.keys()):
            if str(self.dictVarsStatuses[key]) == "True":
                print(Fore.WHITE + str(key), end = ' ')
        print()

        print(Fore.RED + "False are ", end = '')
        for key in sorted(self.dictVarsStatuses.keys()):
            if str(self.dictVarsStatuses[key]) == "False":
                print(Fore.WHITE + str(key), end = ' ')
        print()

    def showUnknownVars(self):
        if len(self.listQueries) == 0:
            print(Fore.RED + "No vars need to explore.")
            return
        print(Fore.MAGENTA + "Need to find " + Fore.WHITE + ", ".join(self.listQueries))

    def showUnexpectedChars(self):
        if len(self.listUnexpectedChars) > 0:
            print(Fore.RED + "Non recognised chars in input constructions -> " + ", ".join(self.listUnexpectedChars) + Fore.WHITE)
        else:
            print(Fore.GREEN + "No unexpected chars were found" + Fore.WHITE)

    def showAll(self):
        self.showEveryRule()
        self.showFacts()
        self.showQueries()
        self.showUnknownVars()
        self.showVarsStatuses()
        self.showUnexpectedChars()

    def showResult(self):
        for var in self.listQueries:
            print(Fore.YELLOW + var + " is " + Fore.GREEN + str(self.dictVarsStatuses[var]))
