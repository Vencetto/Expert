#!/usr/bin/env python
# requires python v >= 3

import sys
import traceback
from parseFile import parse_input
from colorama import init, Fore
from classes import Data
from inputExec import say_hello, got_and_check_input, get_arg_input, flags_full_cycle
from algo import algo


def main():
	init()
	try:
		if len(sys.argv) <= 1:
			say_hello()
			file_input = got_and_check_input()
		else:
			file_input = get_arg_input(sys.argv[1])
		if file_input:
			data = Data()
			parse_input(file_input, data)
			algo(data)
			data.show_result()
			flags_full_cycle(data)
		else:
			print(Fore.RED + "Got no input")
	except KeyboardInterrupt:
		print(Fore.YELLOW + "Shutdown requested...exiting")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)


if __name__ == '__main__':
	main()
