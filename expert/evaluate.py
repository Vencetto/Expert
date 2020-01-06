import re


def peek(stack):
	return stack[-1] if stack else None


def apply_operator(operators, values):
	operator = operators.pop()
	right = values.pop()
	left = values.pop()
	values.append(basic_op(left, operator, right))


def greater_precedence(op1, op2):
	precedences = {'!': 0, '+': 1, '|': 1, '^': 2}
	return precedences[op1] > precedences[op2]


def evaluate(expression):
	tokens = re.findall("[!|^+()]\w+", expression)
	values = []
	operators = []
	for token in tokens:
		if token == '(':
			operators.append(token)
		elif token == ')':
			top = peek(operators)
			while top is not None and top != '(':
				apply_operator(operators, values)
				top = peek(operators)
			operators.pop()  # Discard the '('
		else:
			# Operator
			top = peek(operators)
			while top is not None and top not in "()" and greater_precedence(top, token):
				apply_operator(operators, values)
				top = peek(operators)
			operators.append(token)
	while peek(operators) is not None:
		apply_operator(operators, values)

	return values[0]


print("Got this {0}".format(evaluate("true | false")))


def basic_op(v1, op, v2):
	if op == '+':
		return bool(v1) and bool(v2)
	elif op == '|':
		return bool(v1) or bool(v2)
	elif op == '!':
		return not bool(v2)
	elif op == '^':
		return bool(v1) != bool(v2)
