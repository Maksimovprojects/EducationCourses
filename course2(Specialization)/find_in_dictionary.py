with open ("/Users/max/Desktop/education/Test_record.csv", "r") as raw:
    file = raw.read()
    dic = {}
    for c in file:
        if c not in dic:
            dic[c] = 0
        else:
            dic[c] = dic[c] + 1
print('m: ' + str(dic['m']))
print('M: '+ str(dic['M']))
#---------------------------------------------

eve_nums = []
count = 1
num = 0
while num <= 15:
    eve_nums.append(num)
    count = count + 2
print(eve_nums)
