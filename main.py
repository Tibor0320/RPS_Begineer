# Import the random module to generate computer's choice
import random

# ASCII art for rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store all ASCII art images in a list for easy access
game_images = [rock, paper, scissors]

# Get user's choice (0 for Rock, 1 for Paper, 2 for Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Display the user's choice as ASCII art if it's valid
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# Generate computer's random choice (0-2)
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Game logic to determine winner
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    # Rock beats Scissors
    print("You lose!")
elif computer_choice > user_choice:
    # Paper beats Rock, Scissors beats Paper
    print("You lose!")
elif user_choice > computer_choice:
    # Paper beats Rock, Scissors beats Paper
    print("You win!")
elif computer_choice == user_choice:
    # Same choices result in a draw
    print("It's a draw!")
