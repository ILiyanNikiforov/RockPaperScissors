import random
import pyautogui

list_with_options = ["rock","paper", "scissors"]
list_with_short_names_of_options = ["r", "p", "s"]

computer_move = random.choice(list_with_options)

player_move = pyautogui.prompt(text="Enter your move: "
                                    "[R]ock,[P]aper, [S]cissors: ", title = 'Answer', default='').lower()
while player_move not in list_with_short_names_of_options:
    player_move = pyautogui.prompt(text="Invalid input! Please choose from "
                                        "[R]ock,[P]aper, [S]cissors: ", title='Answer', default='').lower()
if player_move == "r":
    player_move = "rock"
elif player_move == "p":
    player_move = "paper"
elif player_move == "s":
    player_move = "scissors"

if player_move == "rock" and computer_move == "scissors" or\
        player_move == "paper" and computer_move == "rock" or\
        player_move == "scissors" and computer_move == "paper":
    print("You win!")
    print(f'The computer move is {computer_move.capitalize()}!')
elif player_move == computer_move:
    print("Draw!")
else:
    print('You lose!')
    print(f'The computer move is {computer_move.capitalize()}!')
