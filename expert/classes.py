from colorama import Fore

class Data:
    allFacts = ""               # string with input facts
    allQueries = ""             # string with input queries
    dictRules = {}              # dictionary of input rules (string - tuple)
    dictVarsStatuses = {}       # dictionary (var, like 'A' - status, like 'True')
    listUnknownVars = []        # list of vars to find - ?ABC, queries
    listDependencies = []       # list of dependencies for algorithm, what we nned to find to get final answer
    listUnexpectedChars = ()    # list of chars, that we do not expect to apper in constructions or couldn't recognise

    def showFacts(self):
        print(Fore.CYAN + "This was recognised as facts -> " + Fore.WHITE + self.allFacts)

    def showQueries(self):
        print(Fore.CYAN + "This was recognised as queries -> " + Fore.WHITE + self.allQueries)

    def showEveryRule(self):
        if len(self.dictRules) == 0:
            print(Fore.RED + "No rules were recognised")
            return
        for key in self.dictRules:
            print(Fore.YELLOW + "This was recognised as rule -> " + Fore.WHITE + str(key))

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
        if len(self.listUnknownVars) == 0:
            print(Fore.RED + "No vars need to explore.")
            return
        print(Fore.MAGENTA + "Need to find " + Fore.WHITE + ", ".join(self.listUnknownVars))

    def showUnexpectedChars(self):
        if len(self.listOfUnexpectedChars) > 0:
            print(Fore.RED + "Non recognised chars in input constructions -> " + ", ".join(self.listOfUnexpectedChars) + Fore.WHITE)
        else:
            print(Fore.GREEN + "No unexpected chars were found" + Fore.WHITE)

    def showAll(self):
        self.showEveryRule()
        self.showFacts()
        self.showQueries()
        self.showUnknownVars()
        self.showVarsStatuses()
        self.showUnexpectedChars()

    def showresult(self):
        for var in self.listUnknownVars:
            print(Fore.YELLOW + var + " is " + Fore.GREEN + self.dictVarsStatuses[var])
