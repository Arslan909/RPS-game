import random

#Function for user choices
def userCall(userChoice):
    if userChoice == 'R':
        print("You choose rock")
    elif userChoice == 'P':
        print("You choose paper")
    elif userChoice == 'S':
        print("You choose scissors")
        
#Funtion for computer choices
def computerCall(computerChoice):
    if computerChoice == 'R':
        print("computer choose rock")
    
    elif computerChoice == 'P':
        print("computer choose paper")
    
    elif computerChoice == 'S':
        print("computer choose scissors")
        
#Gameplay algorithm
def gamePlay(userChoice, computerChoice):
    if userChoice == computerChoice:
        print("Its a tie")
        
    elif userChoice == 'R' and computerChoice == 'S' or userChoice == 'P' and computerChoice == 'R' or userChoice == 'S' and computerChoice == 'P':
        print("You won ;)")
    
    elif userChoice == 'R' and computerChoice == 'P' or userChoice == 'P' and computerChoice == 'S' or userChoice == 'S' and computerChoice == 'R':
        print("You lose :(")
    
#Main Function 
i=0
round = input("How many times you want to play: ")
round = int(round)

while i < round:      
    userChoice = input("Make your move (r for rock, p for paper, s for scissor): ")#Prompt for user choices
    userChoice = userChoice.upper()  
    
    moves = ["R", "P", "S"]
    computerChoice = random.choice(moves)#Making computer choose
    userCall(userChoice)#passing arguments
    computerCall(computerChoice)
    gamePlay(userChoice, computerChoice)
    i = i+1
    