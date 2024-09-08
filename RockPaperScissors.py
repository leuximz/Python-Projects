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
import random

answer = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. "))
print(answer)

choices = [rock, paper, scissors]
computer = random.choice(choices)
if answer == 0:
    print(rock)
    if computer == rock:
        print(f"I chose {computer}.\nIt's a tie. I'll crush you next time.")
    if computer == paper:
        print(f"I chose {computer}.\nYou win this time, but there will be no next time.")
    if computer == scissors:
        print(f"I chose {computer}.\nYou lose. Amateur.")
elif answer == 1:
    print(paper)
    if computer == rock:
        print(f"I chose {computer}.\nYou lose. Amateur.")
    if computer == paper:
        print(f"I chose {computer}.\nIt's a tie. I'll crush you next time.")
    if computer == scissors:
        print(f"I chose {computer}.\nYou win this time, but there will be no next time.")
elif answer == 2:
    print(scissors)
    if computer == rock:
        print(f"I chose {computer}.\nYou win this time, but there will be no next time.")
    if computer == paper:
        print(f"I chose {computer}.\nYou lose. Amateur.")
    if computer == scissors:
        print(f"I chose {computer}.\nIt's a tie. I'll crush you next time.")
else:
    print("What do you think you're doing? Try again.")
