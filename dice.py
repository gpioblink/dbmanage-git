import random

print("Rolling the dice...")
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print("Die 1:", die1)
print("Die 2:", die2)
print("Total value:", die1 + die2)
print("You won" if die1 + die2 > 7 else "You lose")