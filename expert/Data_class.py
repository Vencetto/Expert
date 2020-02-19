from colorama import Fore
from collections import deque


class Data:
	allFacts = ""               # string with input facts
	allQueries = ""             # string with input queries
	allRules = []               # list of input rules
	dictVarsStatuses = {}       # dictionary (var, like 'A' - status, like 'True')
	listQueries = []            # list of vars to find - ?ABC, queries
	stackDependencies = deque() # deque of dependencies for algorithm, what we need to find to get final answer

	def show_facts(self):
		print(Fore.CYAN + "This was recognised as facts -> " + Fore.WHITE + self.allFacts)

	def show_queries(self):
		print(Fore.CYAN + "This was recognised as queries -> " + Fore.WHITE + self.allQueries)

	def show_every_rule(self):
		if len(self.allRules) == 0:
			print(Fore.RED + "No rules were recognised")
			return
		for rule in self.allRules:
			print(Fore.YELLOW + "This was recognised as rule -> " + Fore.WHITE + rule)

	def show_vars_statuses(self):
		if len(self.dictVarsStatuses) == 0:
			print(Fore.RED + "No vars were recognised.")
			return

		print(Fore.GREEN + "True are ", end='')
		for key in sorted(self.dictVarsStatuses.keys()):
			if str(self.dictVarsStatuses[key]) == "True":
				print(Fore.WHITE + str(key), end=' ')
		print()

		print(Fore.RED + "False are ", end='')
		for key in sorted(self.dictVarsStatuses.keys()):
			if str(self.dictVarsStatuses[key]) == "False":
				print(Fore.WHITE + str(key), end=' ')
		print()

	def show_unknown_vars(self):
		if len(self.listQueries) == 0:
			print(Fore.RED + "No vars need to explore.")
			return
		print(Fore.MAGENTA + "Need to find " + Fore.WHITE + ", ".join(self.listQueries))

	def show_all(self):
		self.show_every_rule()
		self.show_facts()
		self.show_queries()
		self.show_unknown_vars()
		self.show_vars_statuses()

	def show_result(self):
		for var in self.listQueries:
			print(Fore.YELLOW + var + " is " + Fore.GREEN + str(self.dictVarsStatuses[var]))
