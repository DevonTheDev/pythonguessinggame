import os
import sys
from random import randint # Used in random number generator

user_stats = open(os.path.join(sys.path[0], 'user_stats.txt'), 'r+') # Opens the file in the same directory as the executable, makes it easier to manage

table = []
# Wins
# Attempts
# Win Percentage

for lines in user_stats:
    if(lines != ""):
        table.append(int(lines.strip()))


def guess_check(player_guesses, generated_number):
    if(player_guesses > 0):
        user_guess = input("You have " + str(player_guesses) + " guesses left. Please guess a number: ")

        if (int(user_guess) == generated_number):
            print("Congratulations you won")
            table[0] += 1 # Updates the wins counter
            Welcome()
        elif(int(user_guess) > generated_number):
            print("The number you guessed was larger than the correct one")
            player_guesses = player_guesses - 1
            guess_check(player_guesses, generated_number)
        elif(int(user_guess) < generated_number):
            print("The number you guessed was less than the correct one")
            player_guesses = player_guesses - 1
            guess_check(player_guesses, generated_number)
    else:
        print("Sorry, you've run out of guesses. The correct guess was " + str(generated_number))
        Welcome()


def Welcome():
    print("Welcome to the Python Number Guesser Game. Please select one of the following options")
    print("1 - Start the Game")
    print("2 - See your stats")
    print("3 - Exit the Game")

    user_input = int(input("Choose an option here: "))

    if (table[0] > 0):
        table[2] = int(round((int(table[0])/int(table[1])) * 100, 0)) # Updates the win percentage between games so stats menu is correct

    if(user_input == 1):
        table[1] += 1 # Updates the attempts counter
        guess_check(3, randint(1, 9))

    elif(user_input == 2):
        print("Total Wins:", table[0])
        print("Total Attempts:", table[1])
        print("Win Percentage: " + str(table[2]) + "%")
        Welcome()

    elif(user_input == 3):
        print("Thank you for playing!")

        user_stats.seek(0) # Eliminates the white space caused by the .truncate(0)
        user_stats.truncate(0) # Clear the contents of the file so we can update it below

        for line in table:
            user_stats.write(str(line))
            user_stats.write('\n')
        user_stats.close()
        quit()


# Starts the Game
Welcome()
