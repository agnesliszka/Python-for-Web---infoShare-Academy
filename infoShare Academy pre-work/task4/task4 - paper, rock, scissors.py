'''Paper, Rock, Scissors
'''

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message ={"tie": "Yupi it's a tie!",
          "won" : "Hurray you won!",
          "lost" : "Aww you lost!" }

def who_is_the_winner(user_choice, computer_choice):
  print("You choose %s" % user_choice)
  print("The computer chose %s" %computer_choice)
  
  if user_choice == computer_choice:
    print (message['tie'])
  elif user_choice=="ROCK" and computer_choice=="SCISSORS":
    print (message['won'])
  elif user_choice=="PAPER" and computer_choice=="ROCK":
    print (message['won']  )
  elif user_choice=="SCISSORS" and computer_choice=="PAPER":
    print (message['won'])  
  else:
    print (message['lost'])
    
def play():
  user_choice=input("Enter - Rock, Paper, or Scissors: ").upper()
  computer_choice = options[randint(0, 2)]
  who_is_the_winner(user_choice, computer_choice)  

play()
  
