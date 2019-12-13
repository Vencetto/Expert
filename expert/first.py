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
        print(Fore.GREEN + "Write file name: " + Fore.WHITE)
        fileName = input()
        with open(fileName) as file:
            fileContent = file.read()
        print("File closed ? -> " + file.closed) 
        if fileContent:
            return 1
    print(Style.RESET_ALL)
    return 0
        
sayHello()
if not gotAndCheckInput():
    print(Fore.RED + "Got no input." + Style.RESET_ALL)
