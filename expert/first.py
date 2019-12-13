import os
from parseFile import parseInput 
from colorama import init, Fore, Style

def sayHello():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.GREEN +r" ______  __  __   ______  ______   ______  ______     ______   __  __   ______   ______  ______   __    __    |")
    print(r"/\  ___\/\_\_\_\ /\  == \/\  ___\ /\  == \/\__  _\   /\  ___\ /\ \_\ \ /\  ___\ /\__  _\/\  ___\ /\ \-./  \   |")
    print(r"\ \  __\\/_/\_\/_\ \  _-/\ \  __\ \ \  __<\/_/\ \/   \ \___  \\ \____ \\ \___  \\/_/\ \/\ \  __\ \ \ \-./\ \  |")
    print(r" \ \_____\/\_\/\_\\ \_\   \ \_____\\ \_\ \_\ \ \_\    \/\_____\\/\_____\\/\_____\  \ \_\ \ \_____\\ \_\ \ \_\ |")
    print(r"  \/_____/\/_/\/_/ \/_/    \/_____/ \/_/ /_/  \/_/     \/_____/ \/_____/ \/_____/   \/_/  \/_____/ \/_/  \/_/ |")
    print(r"---------------------------------------------------------------------------------------------------------------")
    print(Style.RESET_ALL)

def gotAndCheckInput():
    fileContent = ""

    for retryCounter in range(0, 3):

        print(Fore.GREEN + "Write file name: (q for exit)" + Fore.WHITE)
        fileName = input()
        if fileName == "q" or fileName == "Q":
            return 0

        try:
            with open(fileName) as file:
                fileContent = file.read()
        except IOError:
            print(Fore.RED + f"No such file or directory: '{fileName}'" + Fore.WHITE) 

        if fileContent:
            return fileContent
    return 0

init()
sayHello()
fileInput = gotAndCheckInput()
if fileInput:
    parseInput(fileInput)
else:
    print(Fore.RED + "Got no input")
