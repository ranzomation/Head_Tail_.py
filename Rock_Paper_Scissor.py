import random

inpt = input("Welcome to rock paper scissor game \nright rules to show them or press skip:").lower()
if inpt == 'rules':
  print("the rules are .......................................")


guesses = ['rock','paper','scissor']


guess = random.choice(guesses)


choice = input("what do you want to choose: ").lower()

if choice in guesses :
  if choice == 'rock':
    if guess == 'paper':
      print ('you lose')
    elif guess == 'scissor':
      print ('you win')
    else :
      print ('tie')

  if choice == 'paper':
    if guess == 'rock':
      print ('you win')
    elif guess == 'scissor':
      print ('you lose')
    else :
      print ('tie')

  if choice == 'scissor':
    if guess == 'paper':
      print ('you win')
    elif guess == 'rock':
      print ('you lose')
    else :
      print ('tie')

  