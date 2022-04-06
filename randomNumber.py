# Guess a number between 1 and 100 

import random

num = random.randint(1, 100)
guess = int(input('Guess a number between 1 and 100'))

while guess < num:
    guess = int(input('Guess higher'))

while guess > num:
    guess = int(input('Guess lower'))

print('BINGO')
