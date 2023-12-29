import random
# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______           
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_img =[rock, paper, scissor]
print("Let us play, Rock, Paper, Scissor! ")
user_choice = int(input("Type 0 - Rock, 1 - Paper, 2 - Scissor: "))
if(user_choice >= 3 or user_choice < 0):
  print("You typed invalid number")
else:
  print("You",game_img[user_choice])
  computer_choice = random.randint(0,2)
  print("Computer chose",game_img[computer_choice])

  if(user_choice == 2 and computer_choice == 0):
    print("You lose!")
  elif(user_choice == 0 and computer_choice == 2):
    print("You win!")
  elif(computer_choice > user_choice):
    print("You lose")
  elif(user_choice > computer_choice):
    print("You win!")
  elif(computer_choice == user_choice):
    print("It's a tie!",computer_choice)
    

