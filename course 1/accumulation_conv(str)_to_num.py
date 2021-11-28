addition_str = "2+5+10+20"
addition_num = addition_str.split("+")
addition_int = list(addition_num)
sum_val = 0
for num in addition_int:
    number = int(num)
    sum_val += number
    print(sum_val)
    
