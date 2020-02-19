from colorama import Fore
import re

from constants import REGEXP_QUERIES, REGEXP_FACTS, REGEXP_ONE_RULE, OPS


def parse_input(file_input, data):
	fault = False

	temp_list = re.findall(REGEXP_ONE_RULE, file_input, re.MULTILINE)
	for elem in temp_list:
		if correct_brackets(str(elem)):
			data.allRules.append("".join(elem).strip())
		else:
			print(Fore.RED + '{0} seems to have troubles with brackets,  skipped'.format(str(elem)))  # maybe should check operations to be correct

	if len(data.allRules) == 0:
		print(Fore.YELLOW + "Rules was not found in file")
		fault = True

	facts = re.search(REGEXP_FACTS, file_input)
	if not facts:
		print(Fore.YELLOW + "Facts was not found in file")
		fault = True
	else:
		data.allFacts = str(facts.group(0))

	queries = re.search(REGEXP_QUERIES, file_input)
	if not queries:
		print(Fore.YELLOW + "Queries was not found in file")
		fault = True
	else:
		data.allQueries = str(queries.group(0))

	if fault:
		print(Fore.RED + "Input file component not found")
		return
	else:
		get_queries(data)
		get_known_vars(data)


def correct_brackets(rule):
	open_br = '('
	close_br = ')'
	my_map = dict(zip(open_br, close_br))
	queue = []

	for i in rule:
		if i in open_br:
			queue.append(my_map[i])
		elif i in close_br:
			if not queue or i != queue.pop():
				return 0
	return 1


def get_queries(data):
	for querieChar in data.allQueries:
		if querieChar.isalpha() and querieChar not in data.listQueries:
			data.listQueries.append(querieChar)


def get_known_vars(data):
	for factChar in data.allFacts:
		if factChar.isalpha():
			data.dictVarsStatuses[factChar] = True
