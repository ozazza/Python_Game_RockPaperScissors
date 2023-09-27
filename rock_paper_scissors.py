import random

from colorama import Fore, Back

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

play_again = 'y'
while play_again == 'y':

    # Player's move
    player_move = input(Fore.LIGHTYELLOW_EX + 'Choose [r]ock, [p]aper, [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid input. Try again...')

    # System's move
    computer_random_move = random.randint(1, 3)
    computer_move = ''

    if computer_random_move == 1:
        computer_move = rock
    elif computer_random_move == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.YELLOW + f'The computer chooses {Fore.LIGHTMAGENTA_EX + computer_move}')

    if player_move == computer_move or \
            player_move == computer_move or \
            player_move == computer_move:
        print(Fore.BLUE + 'Draw')
    elif player_move == rock and computer_move == scissors or \
            player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        print(Fore.GREEN + 'You win')
    else:
        print(Fore.RED + 'You lose')

    play_again = input(Fore.RESET + 'Play again y/n: ')
    if play_again == 'n':
        print(Back.LIGHTBLACK_EX + 'Okay, see you!')
        break
