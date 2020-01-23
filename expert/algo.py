from colorama import Fore
from evaluate import evaluate
import re


def algo(data):
	# add first dependencies from queries
	for queryLetter in data.listQueries:
		if queryLetter in data.dictVarsStatuses and data.dictVarsStatuses[queryLetter] == 'False':
			print(Fore.WHITE + '{queryLetter} is searching right now')
			data.stackDependencies.append(str(queryLetter))

			# check if all vars we need is already known
			while len(data.stackDependencies) > 0:

				# go though every rule and find those letters which need to be found
				for rule in data.allRules:

					# if all vars are known and sentence can be calculated
					if check_unknown_vars(rule.replace(' ', ''), data.stackDependencies) == 0:

						if '<=>' in rule:
							solver(rule.split('<=>')[-1], rule.split('=>')[0], data)
						elif '=>' in rule:
							solver(rule.split('<=>')[0], rule.split('=>')[-1], data)

							# this for debug
							data.show_unknown_vars()
							data.show_vars_statuses()

							#   calculate rule and write vars
							# lhs = rule.split('=>')[0].strip().replace(' ', '')
							# rhs = rule.split('=>')[-1].strip().replace(' ', '')

							# write_result(rhs, lhs, data)
							# write_result(lhs, rhs, data)

							# this for debug
							# data.show_unknown_vars()
							# data.show_vars_statuses()

		elif queryLetter in data.dictVarsStatuses and data.dictVarsStatuses[queryLetter] == 'True':
			print(Fore.WHITE + '{queryLetter} is already known as True')


def solver(dest, src, data):


def write_result(src, des, data):
	print('src -> ' + src + '| des -> ' + des + '|')
	result = evaluate(src, data.dictVarsStatuses)
	if result:
		if len(des) == 0 and des.isalpha() and des in data.dictVarsStatuses.keys:
			print('{0} status {1} changed to {2}'.format(des, data.dictVarsStatuses[des], result))
			data.dictVarsStatuses[des] = bool(result)
		else:
			match = re.fullmatch('^\(?[A-Z](\+\(?[A-Z]\)?)*', des)
			if match is not None:  # if destination is in correct form
				print('Got match for {0} -> {1}'.format(des, match.string))
				#for char in des:
				'''-----------###-----------'''
			else:
				print('no match for {0}'.format(des))
	else:
		print('{0} cannot be calculated. Destination not writable'.format(src))


'''
def calculate(rule, data):
	
	if result if undetermined
		undetermined
	if rule.isalpha() and len(rule) == 1            # easy case ,only one letter
		return data.dictVarsStatuses(rule)
	if '!' in rule and len(rule) > 1                # NOT case
		letter = rule.find('!') + 1
		return not data.dictVarsStatuses(letter)
	if '(' in rule and ')' in rule:                 # brackets case
		first_index = rule.find('(')
		second_index = rule.find(')')

		calculate(rule[first_index:second_index])
		# maybe replace with returned value part of string

	if binary operation (a,b):                      # binary operation
        let second = if fact == a then b else a
        if OR and result is false
            false
        if OR and result is true
            if second is false
                true
            else
                undetermined
        if AND and result is true
            true
        if AND and result is false
            if second is true
                false
            else
                undetermined
        if XOR and result is false
            return second
        if XOR and result is true
            not second
	'''


def check_unknown_vars(rule, list):
	# check if in rule exists one of the wanted vars
	if [unknown_var for unknown_var in list if(unknown_var in rule)]:  # check it later

		"""Check whether 'str' contains ANY of the chars in 'set'"""
		''' return 1 in [c in str for c in set]'''

		# DELETE NEXT ROW LATER
		print('found one of the list {0} in {1}'.format(', '.join(list), rule))

		return 1
	else:
		return 0
