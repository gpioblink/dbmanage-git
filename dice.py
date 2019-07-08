import random

print("What is your name?")
name = input("> ")
print("Hello,", name + "!")

print("Rolling the dice...")
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print("Die 1:", die1)
print("Die 2:", die2)
print("Total value:", die1 + die2)