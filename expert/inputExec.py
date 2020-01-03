import os
from colorama import Fore
import tkinter
from tkinter import filedialog


def choose_file_box():
	root = tkinter.Tk()
	root.withdraw()
	return filedialog.askopenfilename()


def say_hello():
	os.system('cls' if os.name == 'nt' else 'clear')

	print(Fore.GREEN + "___________________________________________________________________________________________________________________________________________________")
	print("      :::::::::: :::    ::: :::::::::  :::::::::: ::::::::: :::::::::::          ::::::::  :::   :::  :::::::: ::::::::::: ::::::::::   :::   ::: |")
	print("     :+:        :+:    :+: :+:    :+: :+:        :+:    :+:    :+:             :+:    :+: :+:   :+: :+:    :+:    :+:     :+:         :+:+: :+:+: |")
	print("    +:+         +:+  +:+  +:+    +:+ +:+        +:+    +:+    +:+             +:+         +:+ +:+  +:+           +:+     +:+        +:+ +:+:+ +:+ |")
	print("   +#++:++#     +#++:+   +#++:++#+  +#++:++#   +#++:++#:     +#+             +#++:++#++   +#++:   +#++:++#++    +#+     +#++:++#   +#+  +:+  +#+  |")
	print("  +#+         +#+  +#+  +#+        +#+        +#+    +#+    +#+                    +#+    +#+           +#+    +#+     +#+        +#+       +#+   |")
	print(" #+#        #+#    #+# #+#        #+#        #+#    #+#    #+#             #+#    #+#    #+#    #+#    #+#    #+#     #+#        #+#       #+#    |")
	print("########## ###    ### ###        ########## ###    ###    ###              ########     ###     ########     ###     ########## ###       ###     |")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------\n")


def exe_flags(flags, data):
	if 'l' in flags or 'L' in flags:
		data.show_all()
	else:
		if 'f' in flags or 'F' in flags:
			data.show_facts()
		if 'q' in flags or 'Q' in flags:
			data.show_queries()
		if 'r' in flags or 'R' in flags:
			data.show_every_rule()
		if 'v' in flags or 'V' in flags:
			data.show_vars_statuses()
		if 'u' in flags or 'U' in flags:
			data.show_unknown_vars()
		if 'x' in flags or 'X' in flags:
			data.show_unexpected_chars()


def show_flags():
	print(Fore.GREEN + "\nAnything else ?")
	print(Fore.YELLOW + "\t F -shows all facts")
	print("\t Q -shows all queries")
	print("\t R -shows every rule")
	print("\t V -shows all vars and their statuses")
	print("\t U -shows all unknown variables/queries")
	print("\t X -shows all unexpected chars")
	print("\t L -shows all")
	print("\t N -exit" + Fore.WHITE)


def flags_full_cycle(data):
	show_flags()
	try:
		flags = input()
		if not ('n' in flags or 'N' in flags) and not flags.isspace():
			exe_flags(flags, data)
			flags_full_cycle(data)
	except IOError:
		return 0


def got_and_check_input():
	file_content = ''

	for retryCounter in range(0, 3):

		print(Fore.GREEN + "Write file name: (q for exit OR v for visual mode)" + Fore.WHITE)
		try:
			written_input = input()
		except IOError:
			return 0

		if written_input == "q" or written_input == "Q":
			return 0
		if written_input == "v" or written_input == "V":
			written_input = choose_file_box()

		try:
			with open(written_input) as file:
				file_content = file.read()
		except IOError:
			print(Fore.RED + f"Troubles with reading file: '{written_input}'")

		if file_content:
			return file_content
	return 0


def get_arg_input(file_name):
	file_name = ''

	try:
		with open(file_name) as file:
			file_content = file.read()
	except IOError:
		print(Fore.RED + f"Troubles with reading file: '{file_name}'")

	if not file_content.isspace():
		return file_content
	return ''

