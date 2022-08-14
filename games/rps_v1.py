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

name = input("Your name is: ")

not_finish = False

while not not_finish:

    your_choice = int(input(f'What do you choose {name}? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nPick a correct options or you will lose: '))

    def guess():
        if your_choice >= 3 or your_choice < 0:
          print(f'Hi {name} You pick a invalid number, you lose!')
        else:
          print(f'{name} choice!!!')
          print(game_options[your_choice])

          computer_choice = random.randint(0, 2)
          print("Computer Choice")
          print(game_options[computer_choice])

          if your_choice == 0 and computer_choice == 1:
            print(f'{name} lose!!!')
          elif your_choice == 1 and computer_choice == 2:
            print(f'{name} lose!!!')
          elif your_choice == 2 and computer_choice == 0:
            print(f'{name} lose!!!')
          elif your_choice == computer_choice:
            print("It's a draw!!!")
          else:
            print(f'{name} Win!!!')
    guess()

    should_continue = input(f'Holi {name}. Do you want restart the play?\nType yes or no: ')
    if should_continue == "yes":
        not_finish = False
    elif should_continue == "no":
        not_finish = True
        print(f'Good play! Bye {name}!')