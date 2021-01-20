from random import choice

game = True
symbols = ['rock', 'paper', 'scissors']


def user_choice():
    u_choice = input("\nChoice rock, paper or scissors and press enter.\n")

    while u_choice != 'rock' and u_choice != 'paper' and u_choice != 'scissors':
        u_choice = input("Enter the correct name 'rock', 'paper' or 'scissors'.\n")

    return u_choice


def computer_choice():
    com_choice = choice(symbols)

    return com_choice


def result(u_choice, com_choice):
    if ((u_choice == 'rock' and com_choice == 'rock') or
        (u_choice == 'paper' and com_choice == 'paper') or
        (u_choice == 'scissors' and com_choice == 'scissors')):
            return "Dead-heat"

    elif ((u_choice == 'rock' and com_choice == 'scissors') or
        (u_choice == 'paper' and com_choice == 'rock') or
        (u_choice == 'scissors' and com_choice == 'paper')):
            return "You win!"

    elif ((u_choice == 'rock' and com_choice == 'paper') or
        (u_choice == 'paper' and com_choice == 'scissors') or
        (u_choice == 'scissors' and com_choice == 'rock')):
            return "You lost!"


while game == True:
    u_choice = user_choice()
    com_choice = computer_choice()
    game_result = result(u_choice, com_choice)

    print(f"\nYour choice: {u_choice}.")
    print(f"Computer choice: {com_choice}.")
    print(f"\n{game_result}")

    answer = input(f"\nDo you want to play again? y/n ")

    if answer.lower() != 'y':
        game = False