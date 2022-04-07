# Guess a number between 1 and 100

from random import randint

num = randint(1, 100)
guess = int(input('Guess a number between 1 and 100\n'))

while guess != num:
	if guess > num:
		guess = int(input('Guess lower\n'))
	elif guess < num:
		guess = int(input('Guess higher\n'))

print('BINGO')
