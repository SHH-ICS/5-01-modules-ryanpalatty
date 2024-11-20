# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.

import math

print("The Hypotenuse of a Trianlge is a² + b² = c². ")
print("a = one side")
print("b = other side")
print("c= hypotenuse")
a = float(input("Please Enter First Side: "))
b = float(input("Please Enter Other Side: "))
c = (a**2 + b**2)**0.5
print("The Hypotenuse is: ", c)