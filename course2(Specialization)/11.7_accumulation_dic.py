#The dictionary travel contains the number of countries within each continent that Jackie has traveled to.
#Find the total number of countries that Jackie has been to, and save this number to the variable name total.
#Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for value in travel.values():
    total = total + int(value)
print(total)
#--------------------------------------------------------------------------------------------------
#Write a program that finds the key in a dictionary that has the maximum value.
#If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()

best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

#--------------------------------------------------------------------------------------------------

#Create a dictionary called d that keeps track of all the characters in the string placement
#and notes how many times each character was seen.
#Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
#not correct; not need to call "name" call also char
print(d)
d_list = list(d.keys())
print(d_list)
min_value = d_list[0]
for key_name in d_list:  #not correct; not need to call "name" call also char or key_name
    if d[key_name] < d[min_value]:
        min_value = key_name
print(min_value)


 break
