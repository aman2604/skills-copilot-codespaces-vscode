# import the randome module
import random

# create a list of options that has rock, paper, and scissors
options = ["rock", "paper", "scissors"]

# create a score variable and set it to 0
score = 0

# create a variable to calculate the number of rounds
rounds = 0

# create a while loop run infinitely
while True:

    # create a variable to store the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")

    # create a variable to store the computer's choice
    computer_choice = random.choice(options)

    # print the computer's choice
    print(f"Computer chose {computer_choice}")

# add 1 to the rounds variable 
    rounds += 1

    # check if the user's choice is rock
    if user_choice == "rock":

        # check if the computer's choice is rock
        if computer_choice == "rock":
            print("It's a tie!")
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            print("Computer wins!")
        # check if the computer's choice is scissors
        else:
            print("You win!")
            score += 1

    # check if the user's choice is paper
    elif user_choice == "paper":

        # check if the computer's choice is rock
        if computer_choice == "rock":
            print("You win!")
            score += 1
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            print("It's a tie!")
        # check if the computer's choice is scissors
        else:
            print("Computer wins!")

    # check if the user's choice is scissors
    elif user_choice == "scissors":

        # check if the computer's choice is rock
        if computer_choice == "rock":
            print("Computer wins!")
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            print("You win!")
            score += 1
        # check if the computer's choice is scissors
        else:
            print("It's a tie!")

    # if user enter something else
    else:
        print("Invalid choice!")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # check if the user wants to play again
    # if the user enters no, break the loop
    # if the user enters yes, print the score and continue the loop
    if play_again == "no":
        print(f"Your score is {score}/{rounds}")
        break
    else:
        print(f"Your score is {score}/{rounds}")
        continue
