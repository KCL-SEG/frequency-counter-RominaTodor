# Week 1 Frequencies Exercise.
# Author: Romina Todor.
# Date: 18/10/2023.
# Student Number: k22004116

# Step 1: Input list of no.
# Step 2: Create dictionary for key and value
# Step 3: Item as key (string).
# Step 4: No. items as value (integer).
# Step 5: Output dictionary.

"""ENTER YOUR SOLUTION HERE!"""

"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    return frequencies
"""
from collections import OrderedDict

def frequencies(items):
    frequencies = {}
    myDict = dict()
    """for index, element in enumerate(sorted(map(str, set(items)))):
        myDict[element] = items.count(element)"""
    for item in items:
        item_string = str(item)
        if item_string in myDict:
            myDict[item_string]+=1
        else:
            myDict[item_string]=1
    frequencies = myDict
    return frequencies
