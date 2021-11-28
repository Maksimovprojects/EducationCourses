#Making copy of string

str1 = "I love python"
chars = ""
for letter in str1:
    chars = chars + letter
print(chars)

#Making copy of string to list
str1 = "I love python"
chars = []
for letter in str1:
    chars = chars + [letter]
print(chars)


str1 = "I love python"
chars = []
for letter in str1:
    chars.append(letter)
print(chars)
