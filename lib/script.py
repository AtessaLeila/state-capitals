from capitals import states
import random
from random import sample
from random import shuffle
import sys


play = True

while play:
    score = 0
    print("Welcome to the State Capitals Game!")
    for i in range(0, len(states)):
        random_states1 = random.sample(states, len(states))
        guess = input("Enter the capital of " +
                      random_states1[i]['name'] + ": ")
        if guess == random_states1[i]['capital']:
            score += 1
            random_states1 = random_states1[:-1]
            print("That is correct")
            print("Score: ", score)
        else:
            score -= 1
            random_states1 = random_states1[:-1]
            print('That is incorrect')
            print("Score: ", score)

    again = str(input("Do you want to play again, type yes or no: "))
    if again == "no":
        play = False
        print("Ok, goodbye!")
        sys.exit()
