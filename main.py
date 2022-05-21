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
game_images  = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)
print(game_images[user_choice])

computer = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer])


if user_choice == 0 and computer == 2:
    print("You Win!")
elif user_choice == 2 and computer == paper:
    print("You Win!")
elif user_choice == 1 and computer == 0:
    print("You Win!")