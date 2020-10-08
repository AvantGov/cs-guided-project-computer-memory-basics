"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""


"""
UNDERSTAND: 
    - 

PLAN:
    A = 65
    a = 97
    to convert from uppercase to lowercase, we can add 
    32 to the int representation 
        - then convert back for the decimal representation 
        to the character 
    
    make a results string, init it to be empty 
    iterate through the string 
        if ord(c) is between 65-90
            we need to convert to lowercase 
        otherwise, just move on 
        in both cases, we need to append the character to the result string 



"""

def to_lower_case(string):
    result = ""
    for char in string:
        if 65 <= ord(char) and ord(char) <= 98:
            lowercase = ord(char) + 32
            c = chr(lowercase)
        result += c
    return result 

print(to_lower_case("LLAMA"))