words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for w in words:
    if len(w) > 3:
        num_words += 1
    else:
        print(num_words)
