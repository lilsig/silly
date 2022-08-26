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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

jankenpon = [rock, paper, scissors]

npc = random.randint(0, len(jankenpon)-1)

if (user == 0 and npc == 1) or (user == 1 and npc == 2) or (user == 2 and npc == 0):
    print("You:\n" + jankenpon[user] + "\n")
    print("Computer:\n" + jankenpon[npc] +"\n")
    print("You lose!")
elif (user == 1 and npc == 0) or (user == 2 and npc == 1) or (user == 0 and npc == 2):
    print("You:\n" + jankenpon[user] + "\n")
    print("Computer:\n" + jankenpon[npc] + "\n")
    print("You win!")
elif (user == npc):
    print("You:\n" + jankenpon[user] + "\n")
    print("Computer:\n" + jankenpon[npc] + "\n")
    print("Draw.")
else:
    print("Invalid! Please try again with using only 0, 1, and 2 as your choices.")


