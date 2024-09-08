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

choices = [rock, paper, scissors]

answer = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. "))
print(choices[answer])

computer = random.randint(0, 2)
print("I chose ")
print(choices[computer])

if answer >= 3 or answer < 0:
    print("What do you think you're doing? Try again.")
elif answer == 0 and computer == 2:
    print("You win this time, but there will be no next time.")
elif answer == 2 and computer == 0:
    print("You lose. Amateur.")
elif answer > computer:
    print("You lose. Amateur.")
elif answer < computer:
    print("You win this time, but there will be no next time.")
elif answer == computer:
    print("t's a tie. I'll crush you next time.")
else:
    print("What do you think you're doing? Try again.")
