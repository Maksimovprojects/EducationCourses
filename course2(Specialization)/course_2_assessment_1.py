#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
#Find the total number of characters in the file and save to the variable num.
file = '/Users/max/Desktop/education/Test_record.csv'
file1 = open(file, 'r')
file_lines = file1.readlines()
num = 0
for data in file_lines:
    num = num + len(data)
print(num)
print('Task 1')
file1.close()
#------------------------------------------------------------------------------------------------------
#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#Find the total number of words in the file and assign this value to the variable num_words
#the first
file = open('/Users/max/Desktop/education/Test_record.csv', 'r')
num = 0
for line in file.readlines():
    num = num + len(line.split())
print(num)
file.close()

#the second (runs well)
num_words = 0
fileref = "/Users/max/Desktop/education/Test_record.csv"
with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())
print(num_words)
print('Task 2')
file.close()
#------------------------------------------------------------------------------------------------------

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
#first
file = open('/Users/max/Desktop/education/Test_record.csv', 'r')
a = len(file.readlines())
print(a)

#second
file = open('/Users/max/Desktop/education/Test_record.csv', 'r')
content = file.readlines()
num = 0
for line in content:
    num = num + 1
print(num)
print('Task 3')
file.close()
#------------------------------------------------------------------------------------------------------
#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open ("/Users/max/Desktop/education/Test_record.csv", "r") as file:
    content = file.readline()
    beginning_chars = content[:30]
    print(beginning_chars)
print('Task 4')
file.close()
#------------------------------------------------------------------------------------------------------

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
three = []
with open ("/Users/max/Desktop/education/Test_record.csv", "r") as file:
    for line in file:
        print(line)
        div_line = line.split()
        three = three + [div_line[2]]
print(three)
print('Task 5')
file.close()
#------------------------------------------------------------------------------------------------------

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt
emotions = []
with open ("/Users/max/Desktop/education/Test_record.csv", "r") as file:
    for line in file:
        print(line)
        div_line = line.split()
        #emotions = emotions + [div_line[0]]
        emotions.append(div_line[0])
print(emotions)
print('Task 6')
file.close()
#------------------------------------------------------------------------------------------------------

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

with open ("/Users/max/Desktop/education/Test_record.csv", "r") as raw:
    first_chars = raw.read(33)
    print(first_chars)
print('Task 7')
raw.close()
#------------------------------------------------------------------------------------------------------


#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
#firs way
with open ("/Users/max/Desktop/education/Test_record.csv", "r") as raw:
    o_words = []
    file = raw.read().split()
    for word in file:
        if "m" in word:
            o_words.append(word)
print(o_words)
print('Task 8')
raw.close()
