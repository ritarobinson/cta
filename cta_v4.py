import random

#instructions
print('***  Welcome to Collect Them All!  ***\n\n')
done = False
yes = {'yes', 'y'}
no = {'no', 'n'}
while not done:
    choice = input('Would you like instructions? ').lower()
    if choice in no:
        print
        break
    elif choice in yes:
        print('\nIn Collect Them All you will be trying to collect gems.\n\nAt the start you will decide whether to play on a standard grid - 4 x 4 - or a hard grid - 5 x 5.')
        print('On a standard grid you will have to collect 6 gems to win and on a hard grid you have to collect 10 gems to win.\n\nEach level you will have 3 wrong guesses before it is game over.')
        print('\nOnce the game has started a gem will be randomly placed inside the selected grid.\nIt will stay in that coordinate until it has been guessed correctly.')
        print('\nOnce you have correctly guessed the position of the gem, a new gem will be randomly placed in the grid again, and your score will have gone up.')
        print('This will continue till you have either collected 6 or 10 gems or have made more than 3 wrong guesses.')
        print('\n\nDISCLAIMER: This game could be compared to battleship or whack-a-mole but is an original idea.\nPlease have fun :)\n')
        break
    else:
        print("Please enter 'yes', 'y' or 'no', 'n'.")

print('\n---  GAME START  ---\n')

#lists
grid4 = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
grid5 = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

#variables
gem_collected = 0
guesses = 2
guesses_left = 3
total_gem4 = 6
total_gem5 = 10

#ask which level
done = False
strd = {'standard', 's', '4x4', '4 x 4', '4'}
hard = {'hard', 'h', '5x5', '5 x 5', '5'}
while not done:
    level = input('Which level would you like to play, standard(4x4) or hard(5x5)? ').lower()
    #EASY LEVEL
    if level in strd:
        print('\nLEVEL: Standard   GRID: 4 x 4')
        gemdone = ""
        #generate gem coordinate
        gem4 = random.choice(grid4)
        
        while gemdone != False:
            while not done:
                
                #end of game
                if gem_collected == total_gem4:
                    gemdone = False
                    print('Well done you have collected all gems!')
                    break
                elif guesses_left <= 0:
                    gemdone = False
                    print('GAME OVER')
                    print('You have run out of guesses.')
                    break
                    
                #visual grid
                sgrid = "    A   B   C   D\n\n1   o   o   o   o\n2   o   o   o   o\n3   o   o   o   o\n4   o   o   o   o\n"
                print(sgrid)
                #ask for users guess
                guess = input('Enter your guess: ').upper()
                
                if guess in grid4:
                    #output
                    if guess == gem4:
                        gem_collected += 1
                        print('\nYou got it right!\n')
                        print('Gems collected: {}'.format(gem_collected))
                        print('Gems left: {}'.format(total_gem4 - gem_collected))
                        print('Guesses left: {}\n'.format(guesses_left))
                        #generate gem coordinate
                        gem4 = random.choice(grid4)
                        continue
                        
                    elif guess != gem4:
                        guesses_left -= 1
                        print('\nYou got it wrong :(\n')
                        print('Gems collected: {}'.format(gem_collected))
                        print('Gems left: {}'.format(total_gem4 - gem_collected))
                        print('Guesses left: {}\n'.format(guesses_left))
                        continue

                else:
                    print('Please enter a valid co-ordinate. (i.e A1, B2...)\n')

        
        break

    #HARD LEVEL
    elif level in hard:
        print('\nLEVEL: Hard   GRID: 5 x 5')
        gemdone= ""
        #generate gem coordinate
        gem5 = random.choice(grid5)
        
        while gemdone != False:
            while not done:
                
                #end of game
                if gem_collected == total_gem5:
                    gemdone = False
                    print('Well done you have collected all gems!')
                    break
                elif guesses_left <= 0:
                    gemdone = False
                    print('GAME OVER')
                    print('You have run out of guesses.')
                    break
                    
                #visual grid
                hgrid = "    A   B   C   D   E\n\n1   o   o   o   o   o\n2   o   o   o   o   o\n3   o   o   o   o   o\n4   o   o   o   o   o\n5   o   o   o   o   o\n"
                print(hgrid)
                #ask for users guess
                guess = input('Enter your guess: ').upper()
                
                if guess in grid5:
                    #output
                    if guess == gem5:
                        gem_collected += 1
                        print('\nYou got it right!\n')
                        print('Gems collected: {}'.format(gem_collected))
                        print('Gems left: {}'.format(total_gem5 - gem_collected))
                        print('Guesses left: {}\n'.format(guesses_left))
                        #generate gem coordinate
                        gem5 = random.choice(grid5)
                        continue
                        
                    elif guess != gem5:
                        guesses_left -= 1
                        print('You got it wrong :(\n')
                        print('Gems collected: {}'.format(gem_collected))
                        print('Gems left: {}'.format(total_gem5 - gem_collected))
                        print('Guesses left: {}\n'.format(guesses_left))
                        continue

                else:
                    print('Please enter a valid co-ordinate. (i.e A1, B2...)\n')

        break

    #intro error message
    else:
        print("\nIf you are wanting to play STANDARD level, please enter [ 'standard', 's', '4x4' or '4' ] \nIf you want to play HARD level, please enter [ 'hard', 'h', 5x5' or '5' ]\n")
    
#end message
print('Thank you for playing!')
