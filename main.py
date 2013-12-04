#!/usr/bin/python3

import playmaxit
# import testmaxit
# import curses

def controlMaxit():
    userChoice = 0
    anyKey = 0
    while (userChoice != 2) :
        playmaxit.clearScreen()
        print('Welcome to the Most Awesome Xciting Inside Terminal game (MAXIT)!\n\n'
              'Options\n'
              '\t1. Play Maxit\n'
              '\t2. Exit Maxit\n')
              #'\t3. Test Maxit\n'
        try:
            userChoice = int (input('Enter your choice: '))
            if (userChoice == 1):
                playmaxit.mainMaxit()
            elif (userChoice == 2):
                print('\nThanks for playing MAXIT!\n')
                break
            # elif (userChoice == 3):
            #    testmaxit.testall()
            #    anyKey = input('Testing completed! See log for details. (press enter to continue) ')
        except ValueError:
            anyKey = input('Please enter a valid choice. (press enter to continue) ')

    return

controlMaxit()
