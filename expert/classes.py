from colorama import Fore

class Data:
    allFacts = ""
    allQueries = ""
    dictRules = {}
    dictVarsStatuses = {}
    listUnknownVars = []

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
