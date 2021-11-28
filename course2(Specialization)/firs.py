file = open("../Desktop/education/12345.txt", "r")
for lin in file:
    print(lin.strip())
file.close()
