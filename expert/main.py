#!/usr/bin/env python
import os
from parseFile import parseInput
from colorama import init, Fore, Style

def sayHello():
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


def gotAndCheckInput():
    fileContent = ""

    for retryCounter in range(0, 3):

        print(Fore.GREEN + "Write file name: (q for exit)" + Fore.WHITE)
        writtenInput = input()
        if writtenInput == "q" or writtenInput == "Q":
            return 0
        try:
            with open(writtenInput) as file:
                fileContent = file.read()
        except IOError:
            print(Fore.RED + f"No such file or directory: '{writtenInput}'" + Fore.WHITE) 

        if fileContent:
            return fileContent
    return 0



def main():
    init()
    sayHello()
    fileInput = gotAndCheckInput()
    if fileInput:
        parseInput(fileInput)
    else:
        print(Fore.RED + "Got no input")

if __name__ == '__main__':
    main()
