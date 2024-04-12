"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

a = int(input("input a number\n"))

if a < 0:
    print("This is negative")

elif a > 0:
    print("This is positive")

elif a == 0: 
    print("This is zero")