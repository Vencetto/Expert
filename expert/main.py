#!/usr/bin/env python
#requires python v >= 3

import sys, traceback
from parseFile import parseInput
from colorama import init, Fore, Style
from classes import Data
from inputExec import sayHello, gotAndCheckInput, getArgInput, flagsFullCycle
from 

def main():
    init()
    try:
        if len(sys.argv) <= 1:
            sayHello()
            fileInput = gotAndCheckInput()
        else:
            fileInput = getArgInput(sys.argv[1])
        if fileInput:
            data = Data()
            parseInput(fileInput, data)
            algo(data)
            data.showResult()
            flagsFullCycle(data)
        else:
            print(Fore.RED + "Got no input")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file = sys.stdout)
    sys.exit(0)

if __name__ == '__main__':
    main()
