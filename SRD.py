# "Shoot, Reload, Defend" created by Armin Asadishad 8/31/14 to 9/2/14 completed
# First game made by me. Python 2.7.7
# Everything works! Adding: menu page w/ pygame surface

import sys, random

playerBullets = 0
computerBullets = 0

# Game Menu
    # 'Start' ... 'Press Any Key'
    # Start handles everything. On-Screen: show instructions and About.
    
    
# Play Again function. Everything works! Idk what exactly 'except ValueError: continue' does. 
def gameOver():
    while True:
        playAgain = raw_input('Play Again? ').lower()
        try:
            playAgain = str(playAgain)
            global playerBullets
            playerBullets = 0
            global computerBullets
            computerBullets = 0
        except ValueError:
            continue
        if playAgain == 'y' or playAgain == 'yes': # Why do you have to have 'or' in order for it to work???
            break
        elif playAgain == 'n' or playAgain == 'no':
            sys.exit()
        else:
            print "Invalid key, please enter YES or NO."
        
playing = True
while playing:

# range- It starts at your first parameter and again ends 1 before your second
# range(5,10) would be [5,6...9] range has to be integers
# if computer selects '0' it reloads, if more than '1' bullet it can 'r' or 's'
    for turn in range(200):
        if computerBullets == 0:
            compChoice = random.randint(0,1)
        elif computerBullets > 0:
            compChoice = random.randint(0,2)

    playerChoice = str(raw_input('What do you do this turn? ')).lower()

# Player Settings and Computer Settings (0 is r, 1 is d, 2 is s):
    if playerChoice == 'r':
        playerBullets = playerBullets + 1
        print "Added one bullet.", "You have:", playerBullets, "remaining."
        if compChoice == 0:
            computerBullets = computerBullets + 1
            print "Computer reloaded.", computerBullets, "remaining."
        elif compChoice == 1:
            print "Computer defended itself."
        elif compChoice == 2:
            if playerChoice == 'r':
                print "While reloading the Computer shot and killed you!"
                print "GAME OVER!"
                gameOver() # works but bullets from previous match stay
                # used to be 'playing = False', 'break' closes / ends loop

# Shoot Settings:
    elif playerChoice == 's':
        if playerBullets == 0:
            print "You can't shoot without any bullets!"
        elif playerBullets > 0:
            playerBullets = playerBullets - 1
            print "You shot the computer.", "You have:", playerBullets, "remaining."
            if compChoice == 0:
                print "While Computer reloaded. You shot and killed it."
                print "You have won!"
                gameOver()
            elif compChoice == 1:
                print "Computer defended against your shot." # check -1 from your remaining bullets
            elif compChoice == 2:
                computerBullets = computerBullets - 1 # comp 's' -1 here? or at 'r' elif compChoice statement above?
                print "Both players shot each other and died."
                print "It's a draw!"
                gameOver() # used to be 'playing = False'

# Defend Settings:
    elif playerChoice == 'd':
        print "You have defended yourself."
        if compChoice == 0:
            computerBullets = computerBullets + 1
            print "Computer reloaded while you defended yourself."
        elif compChoice == 1:
            print "Both players defended themselves."
        elif compChoice == 2:
            computerBullets = computerBullets - 1
            print "You defended against Computer's shot."
    
    elif playerChoice == 'q' or playerChoice == 'quit':
        sys.exit()
        
    else:
        print "You haven't selected a choice: R, S, or D."
