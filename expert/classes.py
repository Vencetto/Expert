from colorama import Fore

class Data:
	allRules
	allFacts
	allQueries
	listRules = []

	def showRules();
		print(self.allFacts)

	def showFacts():
		print(self.allFacts)

	def showQueries():
		print(self.allQueries)

	def showEveryRule();
		
		if len(self.listRules) == 0
			print(Fore.RED + "No rules was recognised")
			return 
		
		for elem in self.listRules:
			print(Fore.YELLOW + "This rule was recognisez ->  " + FOre.WHITE + elem)