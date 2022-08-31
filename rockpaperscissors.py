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

#Write your code below this line 👇
user_selection = input("What do you choose? Type 0 for rock, 1 for paper and 2 for Scissors.\n")

if user_selection == '0':
  print(rock)
elif user_selection == '1':
  print(paper)
elif user_selection == '2':
  print(scissors)
else:
  print("Invalid input. Game over!")

print("Computer chose:")
computer_selection = random.randint(0,2)
if computer_selection == 0:
  print(rock)
elif computer_selection == 1:
  print(paper)
else:
  print(scissors)
user_selection = int(user_selection)
if user_selection == 0:
  if computer_selection == 0:
    print("It's a draw!")
  elif computer_selection == 1:
    print("You lose!")
  else:
    print("You win!")
elif user_selection == 1:
  if computer_selection == 0:
    print("You win!")
  elif computer_selection == 1:
    print("It's a draw!")
  else:
    print("You lose!")
elif user_selection == 2:
  if computer_selection == 0:
    print("You lose!")
  elif computer_selection == 1:
    print("You win!")
  else:
    print("It's a draw!")
else:
  print("Invalid input. Game over!")



