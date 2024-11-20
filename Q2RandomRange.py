# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
import math

print("Random Number Picker")
x=input("Enter 1st number: ")
x=int(x)
y=input("Enter 2nd number: ")
y=int(y)
z= random.randrange(x,y) 
print("in between numbers below")
print("Lucky Number Is: ",z)