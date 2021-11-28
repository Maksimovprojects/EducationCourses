#Write a while loop that is initialized at 0 and stops at 15.
#If the counter is an even number, append the counter to a list called eve_nums.
eve_nums = []
count = 0
while count <= 15:
    eve_nums.append(count)
    count = count + 2
print(eve_nums)

#doesn't work
eve_nums = []
n = 0
while n <= 15:
    if n%2==0:
        eve_nums.append(n)
        n = n + 1
print(eve_nums)


# -----------------------------------------------------
# Below, we’ve provided a for loop that sums all the elements of list1.
# Write code that accomplishes the same task, but instead uses a while loop.
# Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]
accum = 0
while len(list1) > 0:
    accum = accum + list1.pop()
print(accum)

#---------------------------------------------------------

#Write a function called stop_at_four that iterates through a list of numbers.
#Using a while loop, append each number to a new list until the number 4 appears.
#The function should return the new list.

def stop_at_four(lst):
    new_lst = []
    step = 0
    while len(lst)>step and lst[step] !=4:
        new_lst.append(lst[step])
        step+=1
    return new_lst
#------------------------------------------------------------

#Write a function, sublist, that takes in a list of numbers as the parameter.
#In the function, use a while loop to return a sublist of the input list.
#The sublist should contain the same values of the original list up until it reaches the number 5
#(it should not contain the number 5).
def sublist(lst):
    sub = []
    idx = 0
    while idx < len(lst):
        if lst[idx] == 5:
            break
        sub.append(lst[idx])
        idx += 1
    return sub

#------------------------------------------------------------

#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing,
#but using a while loop instead of a for loop.
#Assign the accumulated total in the while loop code to the variable sum2.
#Once complete, sum2 should equal sum1.

sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
print(sum1)

idx = 0
sum2 = 0
while idx < len(lst):
    sum2 = sum2 + lst[idx]
    idx = idx + 1
print(sum2)

#------------------------------------------------------------

#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops
#once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings,
#regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned.
#If “bye” is the 5th element, the first 4 are returned.)
#If you want to make this even more of a challenge, do this without slicing

def beginning (lst):
    idx = 0
    lst_10 = []
    while idx < 10:
        if lst[idx] == "bye":
            break
        lst_10.append(lst[idx])
        idx += 1
    return lst_10

#------------------------------------------------------------

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True,
#and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}.
#If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary.
#The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

def test(a, logic = True, dict1 = {2:3, 4:5, 6:8}):
    if logic == True:
        for k, v in dict1.items():
            if int(a) == k:
                return v
    return False

#------------------------------------------------------------

#Write a function called checkingIfIn that takes three parameters.
#The first is a required parameter, which should be a string.
#The second is an optional parameter called direction with a default value of True.
#The third is an optional parameter called d that has a default value of
#{'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}.
#Write the function checkingIfIn so that when the second parameter is True,
#it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third.
#If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
        if a in d:
            return True
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False
#------------------------------------------------------------

#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary,
#input parameter, then the function returns that value, and otherwise, it returns False.
#Follow the instructions in the active code window for specific variable assignmemts


def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('apple', direction = True, d = {})
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('blabla', direction = False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit', direction = True)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = (checkingIfIn('apple', direction = True) + 6)
