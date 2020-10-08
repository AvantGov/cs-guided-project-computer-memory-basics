"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.

Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""

"""
UNDERSTAND 
- look at the roman numerals given and evaluate to the int value 

PLAN 
- create list to hold values 
- for each char in string 
    if M: 
        append 1000
        break 
    if D:
        append 500
        break
    if C:
        append 100
        break 
    if L:
        append 50
        break
    if X:
        append 10
        break 
    if V:
        append 5
        break 
    if I:
        append 1
        break
create sum 
create collector
create index 
for item in list:
    if current > next:
        sum += current
        break
    if current < next:
        collector = current - next
        sum += collector
return sum  
"""

def roman_to_integer(roman):
    int_list = []
    result = 0
    collector = 0
    index = 0
    nxt = index + 1

    for item in roman:
        if item == "M":
            int_list.append(1000)
            break
        if item == "D":
            int_list.append(500)
            break
        if item == "C":
            int_list.append(100)
            break
        if item == "L":
            int_list.append(50)
            break
        if item == "X":
            int_list.append(10)
            break
        if item == "V":
            int_list.append(5)
            break
        if item == "I":
            int_list.append(1)
            break
    print("in_list:", int_list)

    for item in int_list:
        if int_list[nxt] == False:
            break
        
        if item > int_list[nxt]:
            result += item
            break
        if item < int_list[nxt]:
            collector = int_list[nxt] - item
            result += collector
            break
    return result

print(roman_to_integer("MDCLXVI"))
