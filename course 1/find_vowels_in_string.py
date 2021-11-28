#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.
#For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.


#way 1
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for char in s:
    if 'a' in char:
        num_vowels += 1
    elif 'e' in char:
        num_vowels += 1
    elif 'i' in char:
        num_vowels += 1
    elif 'o' in char:
        num_vowels += 1
    elif 'u' in char:
        num_vowels += 1
print(num_vowels)

#way2
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for v in vowels:
    for ch in s:
        if ch == v:
            num_vowels +=1
            
