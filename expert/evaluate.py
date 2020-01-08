import re


def peek(stack):
	print('Got last value from stack {0}'.format(stack[-1] if stack else None))
	return stack[-1] if stack else None


def apply_operator(operators, values, vars_statuses):
	operator = operators.pop()
	print('operator {0} applied'.format(operator))
	right = vars_statuses(values.pop())
	left = vars_statuses(values.pop())
	print('applied {0}{1}{2} = {3}'.format(right, operator, left, basic_op(left, operator, right)))
	values.append(basic_op(left, operator, right))


def greater_precedence(op1, op2):
	precedences = {'!': 0, '+': 1, '|': 1, '^': 2}
	return precedences[op1] > precedences[op2]


def evaluate(expression, vars_statuses):
	tokens = re.findall("[!|^+()]|[A-Z]", expression)
	values = []
	operators = []
	for token in tokens:
		if token == '(':
			operators.append(token)
		elif token == ')':
			top = peek(operators)
			while top is not None and top != '(':
				apply_operator(operators, values, vars_statuses)
				top = peek(operators)
			operators.pop()  # Discard the '('
		else:
			# Operator
			top = peek(operators)
			while top is not None and top not in "()" and greater_precedence(top, token):
				apply_operator(operators, values, vars_statuses)
				top = peek(operators)
			operators.append(token)
	while peek(operators) is not None:
		apply_operator(operators, values, vars_statuses)

	return values[0]


def basic_op(v1, op, v2):
	if op == '+':
		return bool(v1) and bool(v2)
	elif op == '|':
		return bool(v1) or bool(v2)
	elif op == '!':
		return not bool(v2)
	elif op == '^':
		return bool(v1) != bool(v2)
