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
        print('\nAt the start you will decide whether to play on a standard grid or a hard grid.')
        print('On a standard grid you will have to collect 6 gems to win and on a hard grid you have to collect 10 gems to win.\n\nEach level you will have 3 wrong guesses before it is game over.\n')
        print('\nOnce the game has started a gem will be randomly placed inside the selected grid.\n')
        print('Once you have correctly guessed the position of the gem, a new gem will be randomly placed in the grid, and your score will have gone up.')
        print('This will continue till you have either collected 6 or 10 gems or have made more than 3 wrong guesses.')
        break
    else:
        print("Please enter 'yes', 'y' or 'no', 'n'.")

print('\n---  GAME START  ---\n')

#lists
grid4 = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
grid5 = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

#variables
gem_collected = 0
guesses = 3
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
        print(gem4)
        
        while gemdone != False:
            #visual grid
            sgrid = "    A   B   C   D\n\n1   o   o   o   o\n2   o   o   o   o\n3   o   o   o   o\n4   o   o   o   o\n"
            print(sgrid)
            #ask for users guess
            guess = input('Enter your guess: ')
            
            #output
            if guess == gem4:
                gem_collected += 1
                print('\nYou got it right!\n')
                print('Gems collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem4 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                #generate gem coordinate
                gem4 = random.choice(grid4)
                print(gem4)
                
            elif guess != gem4:
                guesses -= 1
                print('\nYou got it wrong :(\n')
                print('Gems collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem4 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                print(gem4)
                
            if gem_collected == total_gem4:
                gemdone = False
                print('Well done you have collected all gems!')
            elif guesses <= 0:
                gemdone = False
                print('GAME OVER')
                print('You have run out of guesses.')
        
        break

    #HARD LEVEL
    elif level in hard:
        print('\nLEVEL: Hard   GRID: 5 x 5')
        gemdone= ""
        #generate gem coordinate
        gem5 = random.choice(grid5)
        print(gem5)
        
        while gemdone != False:
            #visual grid
            hgrid = "    A   B   C   D   E\n\n1   o   o   o   o   o\n2   o   o   o   o   o\n3   o   o   o   o   o\n4   o   o   o   o   o\n5   o   o   o   o   o\n"
            print(hgrid)
            #ask for users guess
            guess = input('Enter your guess: ')
            
            #output
            if guess == gem5:
                gem_collected += 1
                print('\nYou got it right!\n')
                print('Gems collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem5 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                #generate gem coordinate
                gem5 = random.choice(grid5)
                print(gem5)
                
            elif guess != gem5:
                guesses -= 1
                print('You got it wrong :(\n')
                print('Gems collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem5 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                print(gem5)

            #end of game
            if gem_collected == total_gem5:
                gemdone = False
                print('Well done you have collected all gems!')
            elif guesses <= 0:
                gemdone = False
                print('GAME OVER')
                print('You have run out of guesses.')

        break

    #intro error message
    else:
        print("\nIf you are wanting to play STANDARD level, please enter [ 'standard', 's', '4x4' or '4' ] \nIf you want to play HARD level, please enter [ 'hard', 'h', 5x5' or '5' ]\n")
    
#end message
print('Thank you for playing!')
