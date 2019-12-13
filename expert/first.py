import os

def sayHello():
    os.system('cls' if os.name == 'nt' else 'clear')

    from colorama import init, Fore, Style
    init()
    
    print(Fore.GREEN +r" ______  __  __   ______  ______   ______  ______     ______   __  __   ______   ______  ______   __    __    |")
    print(r"/\  ___\/\_\_\_\ /\  == \/\  ___\ /\  == \/\__  _\   /\  ___\ /\ \_\ \ /\  ___\ /\__  _\/\  ___\ /\ \-./  \   |")
    print(r"\ \  __\\/_/\_\/_\ \  _-/\ \  __\ \ \  __<\/_/\ \/   \ \___  \\ \____ \\ \___  \\/_/\ \/\ \  __\ \ \ \-./\ \  |")
    print(r" \ \_____\/\_\/\_\\ \_\   \ \_____\\ \_\ \_\ \ \_\    \/\_____\\/\_____\\/\_____\  \ \_\ \ \_____\\ \_\ \ \_\ |")
    print(r"  \/_____/\/_/\/_/ \/_/    \/_____/ \/_/ /_/  \/_/     \/_____/ \/_____/ \/_____/   \/_/  \/_____/ \/_/  \/_/ |")
    print(r"---------------------------------------------------------------------------------------------------------------")
    print(Style.RESET_ALL)

def gotAndCheckInput():
    from colorama import Fore

    for retryCounter in range(0, 3):

        print(Fore.GREEN + "Write file name: (q for exit)" + Fore.WHITE)
        fileName = input()
        if fileName == "q" or fileName == "Q":
            return 0
        fileContent = ""

        try:
            with open(fileName) as file:
                fileContent = file.read()
        except IOError:
            print(Fore.RED + f"No such file or directory: '{fileName}'" + Fore.WHITE) 

        if fileContent:
            return 1
    return 0

from colorama import Fore, Style        
sayHello()
if not gotAndCheckInput():
    print(Fore.RED + "Got no input")
