import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_choice >= 3 or your_choice < 0:
  print("You pick a invalid number, you lose!")
else:
  print("Your choice!!!")
  print(game_options[your_choice])

  computer_choice = random.randint(0, 2)
  print("Computer Choice")
  print(game_options[computer_choice])

  if your_choice == 0 and computer_choice == 1:
    print("You lose!!!")
  elif your_choice == 1 and computer_choice == 2:
    print("You lose!!!")
  elif your_choice == 2 and computer_choice == 0:
    print("You lose!!!")
  elif your_choice == computer_choice:
    print("It's a draw!!!")
  else:
    print("You Win!!!")