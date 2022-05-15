import random

print('Welcome to Collect Them All!')
print('GAME START')

#lists
grid4 = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
grid5 = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

#variables
gem_collected = 0
guesses = 3
total_gem4 = 6
total_gem5 = 10

#ask which level
done = False
strd = {'standard', 's', '4x4'}
hard = {'hard', 'h', '5x5'}
while not done:
    level = input('Which level would you like to play, standard(4x4) or hard(5x5)? ')
    if level in strd:
        print('Level: Standard   Grid: 4 x 4')
        gemdone = ""
        while gemdone != False:
            #generate gem coordinate
            gem4 = random.choice(grid4)
            #ask for users guess
            guess = input('Enter your guess: ')
            #output
            if guess == gem4:
                gem_collected += 1
                print('You got it right!')
                print('Collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem4 - gem_collected))
                print('Guesses left: {}'.format(guesses))
            elif guess != gem4:
                guesses -= 1
                print('You got it wrong.')
                print('Collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem4 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                
            if gem_collected == total_gem4:
                gemdone = False
                print('Well done you have collected all gems!')
            elif guesses <= 0:
                gemdone = False
                print('GAME OVER')
                print('You have run out of guesses.')
        
        break
    
    elif level in hard:
        print('Level: Hard   Grid: 5 x 5')
        gemdone= ""
        while gemdone != False:
            #generate gem coordinate
            gem5 = random.choice(grid5)
            #ask for users guess
            guess = input('Enter your guess: ')
            #output
            if guess == gem5:
                gem_collected += 1
                print('You got it right!')
                print('Collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem5 - gem_collected))
                print('Guesses left: {}'.format(guesses))
            elif guess != gem5:
                guesses -= 1
                print('You got it wrong.')
                print('Collected: {}'.format(gem_collected))
                print('Gems left: {}'.format(total_gem5 - gem_collected))
                print('Guesses left: {}'.format(guesses))
                
            if gem_collected == total_gem5:
                gemdone = False
                print('Well done you have collected all gems!')
            elif guesses <= 0:
                gemdone = False
                print('GAME OVER')
                print('You have run out of guesses.')
        
        break

print('Thank you for playing!')
