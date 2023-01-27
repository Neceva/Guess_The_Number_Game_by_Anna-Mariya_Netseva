import random

computer_num = random.randint(1, 100)
player_num = 0
while True:
    user_input = input("\033[39mGuess the number (between 1 and 100): ")
    if not user_input.isdigit():
        print("Invalid input. Try again!")
        continue
    player_num = int(user_input)
    if player_num == computer_num:
        print(f"\033[46m\033[30mYou guess it! The number is {computer_num}!")
        player_input = input("\033[49m\033[39mDo you want to play again?(Yes/No) ")
        if player_input == "No":
            break
        elif player_input == "Yes":
            computer_num = random.randint(1, 100)
            continue
    elif player_num > computer_num:
        print("\033[31mToo High! Try again...")
    else:
        print(f"\033[31mToo Low! Try again!")