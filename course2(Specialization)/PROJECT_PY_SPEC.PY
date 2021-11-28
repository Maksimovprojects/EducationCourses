# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv
# which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
# We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt
                                                                                        and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# You will create a csv file, which contains columns for the Number of Retweets, Number of Replies,
# Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet),
# and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets,
# and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word,
# and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    for sym in punctuation_chars:
        str1 = str1.replace(sym, '')
    return str1

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_pos(raw_twit_str):
    count = 0
    twit_no_symb = strip_punctuation(raw_twit_str)
    twit_sentence = twit_no_symb.lower()
    for word in twit_sentence.split():
        if word in positive_words:
            count += 1
    return count


def get_neg(raw_twit_str):
    count = 0
    twit_no_symb = strip_punctuation(raw_twit_str)
    twit_sentence = twit_no_symb.lower()
    for word in twit_sentence.split():
        if word in negative_words:
            count += 1
    return count


#--------------------------------------------------------
#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv
#which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet,
#and the number of replies to that tweet). Your task is to build a sentiment classifier,
#which will detect how positive or negative each tweet is. Copy the code from the code windows above,
#and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv,
#which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet),
#Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall)
#for each tweet. The file should have those headers in that order. Remember that there is another component to this project.
#You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets.
#Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

f=open('project_twitter_data.csv','r')
rd=f.readline()
file=open('resulting_data.csv','w')
file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
file.write('\n')
for data in f.readlines():
    data1=data.split(",")
    row_string = '{},{},{},{},{}'.format(int(data1[1]),int(data1[2]),get_pos(data),get_neg(data),(get_pos(data)+get_neg(data)) )
    file.write(row_string)
    file.write('\n')
file.close()
f.close()





Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score
3,0,0,0,0
1,0,2,-2,0
1,2,1,0,1
3,1,1,0,1
6,0,2,0,2
9,5,2,0,2
19,0,2,0,2
0,0,0,-3,-3
0,0,0,-2,-2
82,2,4,0,4
0,0,0,-1,-1
0,0,1,0,1
47,0,1,0,1
2,1,1,0,1
0,2,1,0,1
0,0,2,-1,1
4,6,3,0,3
19,0,2,-1,1
0,0,1,-1,0
