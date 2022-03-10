''' MODULE FOR THE ROCK, PAPER, SCISSORS GAME '''
# An Infinite Rolling CLI Menu Sub-Sequence has also been provided for Player's attraction, attention and ease. #
# All the Unchecked Exceptions generating have also been handeled here #


from random import randint


def RPS_Game():
    print('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
    try:
        player_choice = int(input())
        if player_choice in (0, 1, 2):
            computer_choice = randint(0, 2)
            print('Computer chose', computer_choice)
            if player_choice == computer_choice:
                print("It's a tie!\n")
                status = input("Press 'Y/y' to play again and 'N/n' or any other Key to Exit the Rock, Paper, Scissors game...\n")
                if status in ('Y', 'y'):
                    RPS_Game()
                else:
                    print('Exiting...\n')
            else:
                if str(player_choice) + str(computer_choice) in ('02', '10', '21'):
                    print('Yay! You won!\n')
                    status = input("Press 'Y/y' to play again and 'N/n' or any other Key to Exit the Rock, Paper, Scissors game...\n")
                    if status in ('Y', 'y'):
                        print()
                        RPS_Game()
                    else:
                        print('\nExiting the Rock, Paper, Scissors game...\n')
                else:
                    print('Oops! You lost. Can try again...\n')
                    status = input("Press 'Y/y' to try again and 'N/n' or any other Key to Exit the Rock, Paper, Scissors game...\n")
                    if status in ('Y', 'y'):
                        print()
                        RPS_Game()
                    else:
                        print('Exiting the Rock, Paper, Scissors game...\n')
        else:
            print('Whoops! Invalid Input. Choose among 0, 1 or 2. Please try again...\n')
            RPS_Game()
    except (Exception,):
        print('Oops! Invalid Input! Please try again...\n')
        RPS_Game()


