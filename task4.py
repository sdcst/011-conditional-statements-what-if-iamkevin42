#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""

a = input("Enter a sentence\n")

if "password" in a:
    print("This sentence has the word password in it")

elif "password" not in a:
    print("This sentence does not have the word password in it")