#COLLECT THEM ALL - 2022


import random

#FUNCTIONS

#grid formatting function - no.1
def grid(userGuess):
    row = userGuess[1]

    global Glevel
    global Gstrd
    global Ghard

    #standard changed grid format
    if Glevel in Gstrd:
        columns = "   A B C D"
        blank = "{} o o o o"
        
        if row == "1":
            print(columns,"\n",gridtable(userGuess),"\n",blank.format(2),"\n",blank.format(3),"\n",blank.format(4),"\n")
            
        elif row == "2":
            print(columns,"\n",blank.format(1),"\n",gridtable(userGuess),"\n",blank.format(3),"\n",blank.format(4),"\n")
            
        elif row == "3":
            print(columns,"\n",blank.format(1),"\n",blank.format(2),"\n",gridtable(userGuess),"\n",blank.format(4),"\n")

        elif row == "4":
            print(columns,"\n",blank.format(1),"\n",blank.format(2),"\n",blank.format(3),"\n",gridtable(userGuess),"\n")

    #hard changed grid format
    elif Glevel in Ghard:
        columns = "   A B C D E"
        blank = "{} o o o o o"
        
        if row == "1":
            print(columns,"\n",gridtable(userGuess),"\n",blank.format(2),"\n",blank.format(3),"\n",blank.format(4),"\n",blank.format(5),"\n")
            
        elif row == "2":
            print(columns,"\n",blank.format(1),"\n",gridtable(userGuess),"\n",blank.format(3),"\n",blank.format(4),"\n",blank.format(5),"\n")
            
        elif row == "3":
            print(columns,"\n",blank.format(1),"\n",blank.format(2),"\n",gridtable(userGuess),"\n",blank.format(4),"\n",blank.format(5),"\n")

        elif row == "4":
            print(columns,"\n",blank.format(1),"\n",blank.format(2),"\n",blank.format(3),"\n",gridtable(userGuess),"\n",blank.format(5),"\n")

        elif row == "5":
            print(columns,"\n",blank.format(1),"\n",blank.format(2),"\n",blank.format(3),"\n",blank.format(4),"\n",gridtable(userGuess),"\n")

#grid formatting function - no.2
def gridtable(userGuess):

    #initialising variables
    column = userGuess[0]
    row = userGuess[1]
    table = {"A":0, "B":1, "C":2, "D":3, "E":4}
    place = ["o","o","o","o","o"]
    
    place[table[column]] = "x"

    global Glevel
    global Gstrd
    global Ghard

    #formatting crossed out place
    if Glevel in Gstrd:
        return("{} {} {} {} {}".format(row,place[0],place[1],place[2],place[3]))

    elif Glevel in Ghard:
        return("{} {} {} {} {} {}".format(row,place[0],place[1],place[2],place[3],place[4]))

#output function
def evaluate_guess(guess, default, totals, grids = []):

    #global variables
    global Ggem_collected
    global Gguesses_left
    global Ggem1
    global Ggem2
    global Ggem3
    global Galready_guessed

    #making sure it's a valid guess
    if guess in grids:

        #correct guess
        if guess == Ggem1 or guess == Ggem2 or guess == Ggem3:
            Ggem_collected += 1
            Galready_guessed.clear()
            statement("** Hit! You've collected a gem. **", '*')
            print('\n---  STATS  ---\n')
            print('Hits left: {}'.format(Gguesses_left))
            print('Gems collected: {}'.format(Ggem_collected))
            print('Gems left: {}\n\n'.format(totals - Ggem_collected))
            #generate gem coordinate
            Ggem1 = random.choice(grids)
            Ggem2 = random.choice(grids)
            Ggem3 = random.choice(grids)
            print(default)
            

        elif guess != Ggem1 or guess != Ggem2 or guess != Ggem3:
                        
            #duplicate error message [USABILITY TESTING - making sure user knows how to use game properly]
            if guess in Galready_guessed:
                statement('!! You have already guessed that !!', '!')

            #wrong guess
            else:
                Gguesses_left -= 1
                statement("== You missed! That square doesn't have a gem. ==", '=')

            Galready_guessed.append(guess)

            #prints game stats
            print('\n---  STATS  ---\n')
            print('Hits left: {}'.format(Gguesses_left))
            print('Gems collected: {}'.format(Ggem_collected))
            print('Gems left: {}\n'.format(totals - Ggem_collected))
            print('PREVIOUSLY GUESSED: ', ', '.join(Galready_guessed), '\n\n')
            #changed grid
            grid(guess)

#guess error checking function [USABILITY TESTING - making sure user knows how to use game properly]
def guess_check(question, list):
    while True:
        try:
            response = input(question).upper()
            #check response
            if response not in list:
                print('Please enter a valid coordinate. (i.e A1, B2...)')
                print('Be careful of unwanted spaces! :)\n')
                continue
        except ValueError:
            print
        return response
    

#pretty output statments
def statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))


#MAIN CODE

#setting up loop for play again
keep_going = ""
while keep_going == "":

    #initialising variables
    #constants
    TOTAL_GEM4 = 6
    TOTAL_GEM5 = 10

    #global variables
    Galready_guessed = []
    Ggem_collected = 0
    Gguesses_left = ""
    Ggem1 = ""
    Ggem2 = ""
    Glevel = ""
    Gstrd = {'standard', 's', '4x4', '4 x 4', '4'}
    Ghard = {'hard', 'h', '5x5', '5 x 5', '5'}

    #lists
    grid4 = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
    grid5 = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

    #intro + instructions [USABILITY TESTING - making sure user knows what to do]
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
            print('\n\nIn Collect Them All you will be trying to collect gems.\n')
            print('\nAt the start you will decide whether to play on a standard grid - 4 x 4 - or a hard grid - 5 x 5.')
            print('\n--- Standard ---\nOn a STANDARD grid you will have to collect 6 gems to win.\nYou have 8 wrong guesses before it is Game Over.')
            print('\n--- Hard ---\nOn a HARD grid you have to collect 10 gems to win.\nYou will have 13 wrong guesses till Game Over.\n')
            print('\n- Once the game has started 3 gems will be randomly placed inside the selected grid.\nThey will stay in that coordinate until one has been guessed correctly.')
            print('\n- Once you have correctly guessed the position of one of the gems, new gems will be randomly placed in the grid again, and your score will have gone up.')
            print('This will continue till you have either collected 6 or 10 gems, or have exceeded the defined wrong guesses.')
            print('\n\nPlease have fun :)\n')
            break
        else:
            print("\nPlease enter 'yes', 'y' or 'no', 'n'.")
            print('Be careful of unwanted spaces! :)\n')

    print('\n---  GAME START  ---\n')

    #ask user which level to play
    done = False
    while not done:
        Glevel = input('Which level would you like to play, standard(4x4) or hard(5x5)? ').lower()

        #EASY LEVEL
        if Glevel in Gstrd:
            Gguesses_left = 8
            print('\nLEVEL: Standard   GRID: 4 x 4\n\n')
            gemdone = ""
            #generate gem coordinate
            Ggem1 = random.choice(grid4)
            Ggem2 = random.choice(grid4)
            Ggem3 = random.choice(grid4)
            #visual default grid
            sgrid = "   A B C D\n 1 o o o o\n 2 o o o o\n 3 o o o o\n 4 o o o o\n"
            print(sgrid)
            
            while gemdone != False:
                while not done:
                    
                    #end of game mechanics
                    if Ggem_collected == TOTAL_GEM4:
                        gemdone = False
                        print('GAME OVER')
                        statement('~~ Well done, you have collected all gems! ~', '~')
                        break
                    elif Gguesses_left <= 0:
                        gemdone = False
                        print('GAME OVER')
                        statement('-- You have run out of guesses. --', '-')
                        break
                        
                    #ask for users guess
                    guess = guess_check('Enter your guess: ', grid4).upper()

                    #calling and passing output function
                    evaluate_guess(guess,sgrid,TOTAL_GEM4,grid4)

            break


        #HARD LEVEL
        elif Glevel in Ghard:
            Gguesses_left = 13
            print('\nLEVEL: Hard   GRID: 5 x 5\n\n')
            gemdone= ""
            #generate gem coordinate
            Ggem1 = random.choice(grid5)
            Ggem2 = random.choice(grid5)
            Ggem3 = random.choice(grid5)
            #visual default grid
            hgrid = "   A B C D E\n 1 o o o o o\n 2 o o o o o\n 3 o o o o o\n 4 o o o o o\n 5 o o o o o\n"
            print(hgrid)
                
            while gemdone != False:
                while not done:
                        
                    #end of game mechanics
                    if Ggem_collected == TOTAL_GEM5:
                        gemdone = False
                        print('GAME OVER')
                        statement('~~ Well done, you have collected all gems! ~', '~')
                        break
                    elif Gguesses_left <= 0:
                        gemdone = False
                        print('GAME OVER')
                        statement('-- You have run out of guesses. --', '-')
                        break
                            
                    #ask for users guess
                    guess = guess_check('Enter your guess: ', grid5).upper()

                    #calling and passing output function
                    evaluate_guess(guess,hgrid,TOTAL_GEM5,grid5)

            break

        #intro error message [USABILITY TESTING - making sure user knows how to use game properly]
        else:
            print("\nIf you are wanting to play STANDARD level, please enter [ 'standard', 's', '4x4' or '4' ] \nIf you want to play HARD level, please enter [ 'hard', 'h', '5x5' or '5' ]\n")
            print('Be careful of unwanted spaces! :)\n')

    #loop for play again
    keep_going = input('\nIf you would like to play again press <enter> or any key + <enter> to quit: ')
    print('\n')
    
#end message
print('Thank you for playing!')
