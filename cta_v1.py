import random

#lists
grid = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']

#variables
gem_collected = 0
guesses = 3
total_gem = 6

#main code
done = False
while not done:
    gemdone = ""
    while gemdone != False:
        #generate gem coordinate
        gem = random.choice(grid)
        #ask for users guess
        guess = input('Your guess: ')
        #output
        if guess == gem:
            gem_collected += 1
            print('Right')
            print('Collected {}'.format(gem_collected))
            print('gems left {}'.format(total_gem - gem_collected))
            print('Guesses left {}'.format(guesses))
        elif guess != gem:
            guesses -= 1
            print('Wrong.')
            print('Collected {}'.format(gem_collected))
            print('gems left {}'.format(total_gem - gem_collected))
            print('Guesses left {}'.format(guesses))
                    
        if gem_collected == total_gem:
            gemdone = False
            print('You have collected all gems')
        elif guesses <= 0:
            gemdone = False
            print('game over')
            
    break
