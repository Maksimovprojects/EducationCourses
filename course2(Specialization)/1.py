def sublist(lst):
    n = 0
    sub_lst = []
    while lst[n] != 5:
        sub_lst.append(lst[n])
        n = len(lst) - 1
    return sub_lst
lst = [1, 2, 3, 6, 7, 8, 9]
print(sublist(lst))


def multiply(str1, mult_int = 10):
    str2 = (str1*mult_int)
    return str2
print(multiply('Hello', 3))
