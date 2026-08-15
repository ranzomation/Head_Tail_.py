import random

print('welcome to the coin guessing game!')
guess = int(input('''choose a method to toss the coin:
1. using random.random()
2. using random.randint()
enter your choice 1 or 2 :'''))


if guess == 1 :
  comp = random.random()
  if comp < 0.5 :
    u = "heads"
  else :
    u = "tails"

elif guess == 2 :
  comp = random.randint(0,1)
  if comp == 0 :
    u = "heads"
  else :
    u = "tails"

else :
  print ("please enter 1 or 2")



choice = input("enter your guess (heads or tails):").lower()

if choice == u : 
  print ("you win")

else : 
  print ("you lost")

print (f"your guess was {choice}")
print (f"comp guess was {u} ")