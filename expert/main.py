#!/usr/bin/env python
#requires python v >= 3
import os
import sys, traceback
from parseFile import parseInput
from colorama import init, Fore, Style
from classes import Data
import tkinter
from tkinter import filedialog

def chooseFileBox():
    root = tkinter.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


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

        print(Fore.GREEN + "Write file name: (q for exit OR v for visual mode)" + Fore.WHITE)
        try:
            writtenInput = input()
        except IOError:
            return 0

        if writtenInput == "q" or writtenInput == "Q":
            return 0
        if writtenInput == "v" or writtenInput == "V":
            writtenInput = chooseFileBox()

        try:
            with open(writtenInput) as file:
                fileContent = file.read()
        except IOError:
            print(Fore.RED + f"Troubles with reading file: '{writtenInput}'") 

        if fileContent:
            return fileContent
    return 0



def main():
    try:
        init()
        sayHello()
        fileInput = gotAndCheckInput()
        if fileInput:
            data = Data()
            parseInput(fileInput, data)
            #data.showAll()
            algo(data)
        else:
            print(Fore.RED + "Got no input")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
            
    

if __name__ == '__main__':
    main()
