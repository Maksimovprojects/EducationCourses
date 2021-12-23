def print_wrapper(text):
    with open("test.txt", "w") as f: # "w" rewrite content of file, "a" = append to file, "r" read file
        print(text, file=f, end="-")
print_wrapper("Work hard")
