# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Terry Evans
# Creation Date: 2-10-2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
        cave = ''
        #inconsitent use of tabs and spaces
        while cave != '1' and cave != '2':
                #inconsitent use of tabs and spaces
                print('Which cave will you go into? (1 or 2)')
                #inconsitent use of tabs and spaces
                cave = input()
        #inconsitent use of tabs and spaces
        #NameError: name 'caves' is not defined. Did you mean: 'cave'?
        return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#Note says sleep for 2 seconds but time.sleep is for 3
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
                #missing parenthesis
		print ('Gobbles you down in one bite!')

playAgain = 'yes'
#Invalid syntax did you mean ==
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	#NameError: name 'choosecave' is not defined. Did you mean: 'chooseCave'?
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
                #Did you mean to say "Thanks for playing" or "Thanks for planing"?
		print("Thanks for planing")

