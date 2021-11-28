# 16.3.2.Below, we have provided a list of strings called nums.
#Write a function called last_char that takes a string as input, and returns only its last character.
#Use this function to sort the list nums by the last digit of each number, from highest to lowest,
# and save this as a new list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str1):
    return str1[-1]

nums_sorted = sorted(nums, reverse = True, key = last_char)

#----------------------------------------------------------------------------------------------------

#16.4.4. Sort the following dictionary’s keys based on the value from highest to lowest.
#Assign the resulting value to the variable sorted_values.


dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary.keys(), key = lambda a: dictionary[a], reverse = True)

#----------------------------------------------------------------------------------------------------









lst1 = ["A", "B", "C,", "e", "c", "A", "A", "M"]
d = {}
for char in lst1:
    if char in d:
        d[char] = d[char] + 1
    else:
        d[char] = 1
print(d)
