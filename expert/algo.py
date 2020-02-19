from colorama import Fore
from evaluate import evaluate


def algo(data):
	# add first dependencies from queries
	for queryLetter in data.listQueries:
		if queryLetter not in data.dictVarsStatuses:
			print(Fore.WHITE + f'{queryLetter} is searching right now, added to stack')
			data.stackDependencies.append(str(queryLetter))

			# check if all vars we need is already known
			while len(data.stackDependencies) > 0:
				print(Fore.YELLOW + 'Len stack: {0}'.format(len(data.stackDependencies)))

				# go though every rule and find those letters which need to be found
				for rule in data.allRules:
					print(f'Working with {rule}')

					# if last value exist in rule
					if can_be_found(rule, str(data.stackDependencies[-1])):
						print(Fore.CYAN + 'can be found {0} in {1}'.format(data.stackDependencies[-1], rule))

						# if all vars are known and sentence can be calculated
						if not exist_unknown_vars(rule.replace(' ', ''), data.dictVarsStatuses):
							print('no unknown vars')

							if '<=>' in rule:
								to_calc = rule.split('<=>')[1]
								to_write = rule.split('<=>')[0]
							else:
								to_write = rule.split('=>')[1]
								to_calc = rule.split('=>')[0]

							# evaluate
							hz = evaluate(to_calc, data.dictVarsStatuses)
							print(Fore.GREEN + f'{to_calc} evaluated as {hz}')
							# evaluate writing side
							hz2 = evaluate(to_write, data.dictVarsStatuses)
							print(f'{to_write} evaluated as {hz2}')

							# delete from stack
							print(Fore.RED + 'popped {0}'.format(data.stackDependencies.pop()))

							# this for debug
							data.show_unknown_vars()
							data.show_vars_statuses()

						# add letter to stack for searching
						else:
							data.stackDependencies.append(first_unknown_letter(rule.replace(' ', ''), data))
							print('Added {0} to stack'.format(bool(data.stackDependencies[-1])))

				# default 'False'
				if data.stackDependencies[-1] not in data.dictVarsStatuses:
					data.dictVarsStatuses[data.stackDependencies[-1]] = 'False'
					print(Fore.RED + 'Default false {0}'.format(data.stackDependencies[-1]))


def first_unknown_letter(rule, data):
	for char in rule:
		if char.isalpha():
			data.stackDependencies.append(char)
			return 1
	return 0


def can_be_found(rule, letter):
	if '<=>' in rule:
		if letter in rule.split('<=>')[1]:
			return 1
		else:
			return 0
	elif '=>' in rule:
		if letter in rule.split('<=>')[0]:
			return 1
		else:
			return 0


def exist_unknown_vars(rule, list):
	for char in rule:
		if char in list:
			# DELETE NEXT ROW LATER
			print('found {0} from rule {1} in list of unknown vars {2}'.format(char, rule, ', '.join(list)))
			return 1
	else:
		return 0
