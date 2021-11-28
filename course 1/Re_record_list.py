#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for num in lst_nums:
    larger_nums.append(float(num*2))
print(larger_nums)


#Challenge Now do the same as in the previous problem, but do not create a new list.
#Overwrite the list numbs so that each of the original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
for num in range(len(numbs)):
    numbs[num] = numbs[num]  + 5
print(numbs)


#Given the list of numbers, numbs, create a new list of those same numbers increased by 5.
#Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist = []
for num in numbs:
    newlist.append(int(num) + 5)
print(newlist)


#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for word in verbs:
    ing.append(word + 'ing')
print(ing)
