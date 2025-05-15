'''
snake = 1
gun = -1
water = 0
'''
import random

def check_win(computer , player):
    if(player == computer):
        return "draw"
    elif(player == "snake" and computer == "gun"):
        return "you win"
    elif(player == "gun" and computer == "water"):
        return "you win"
    elif(player == "snake" and computer == "water"):
        return "you win"
    else:
        return "you lose"
    
    
  # list of possible choices  
choices = ["snake", "gun", "water"]

# starting the game
print("\nSnake Water gun game")
print("Type 'snake' , 'gun' , or 'water' to play game . Type 'quit' to stop game")



while True:
    player = input("your turn = ").lower()
    
    if(player == "quit"):
        print("Thanks for playing :")
        break
    
    if player not in  choices:
        print("Invalid choise . try again \n")
        continue
    
    computer = random.choice(choices)
    print(f"computer choise : {computer}")
    
    result = check_win(computer , player)
    print(result + "\n")
    print("" *30)