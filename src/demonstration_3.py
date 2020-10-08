"""
Given a list of integers `lst`, any integer with a frequency that is equal to 
its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. 
If the array contains multiple lucky integers, return the largest one. 
If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""


"""
UNDERSTAND: 
if the count = value, return the value 

PLAN 
define the output variable
sort the list from the largest to the smallest 
make a set 
iterate through the set, counting the # of times each value shows up 
make a count variable 
check if the count == the value 
    if it does, add it the out put variable 
if nothing matches, return -1 

"""
def find_lucky(lst):
    # define the output variable 
    output = -1
    # sort from largest to smallest 
    lst.sort(reverse=True)
    # create a set 
    set_list = set(lst)

    # iterate throught eh set, counting the # of times each value shows up 
    for number in set_list:
        # create the counter 
        count = lst.count(number)
        # check if the count == the value 
        if number == count: 
            # if it does, add it the output variable 
            output = number
    
    # if no matches, return output (or return summative output)
    return output

