"""""""""""""""""""""""""""""""""""""""
 This program is a guessing game.

 @author Omar Barazanji
 @version 2018
 
"""""""""""""""""""""""""""""""""""""""
import random

guesses = 0
remaining = 5
num = random.randint(1, 99)

while (guesses < 5):
	guess = int(raw_input('Enter a random number from 1 - 99: '))
	guesses += 1
	remaining -= 1
	if guess == num:
		print('Correct! You won!')
		print('Thank you for playing...')
		break
	elif guess < num:
		print('Wrong! You have %d tries remaning' % remaining)
		print('You guessed too low')
	elif guess > num:
		print('Wrong! you have %d tries remaining' % remaining)
		print('you guessed too high')
if guesses == 5:
	print('You ran out of guesses! The secret number was: %d' % num)
	print('Thank you for playing...')
