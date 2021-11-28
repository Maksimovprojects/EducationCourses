score = input("Enter Score: ")
g = float(score)
if g > 1:
  print("Error. Enter value between 0.0 and 1.0")
  quit()
elif g < 0:
  print("Error. Enter value between 0.0 and 1.0")
  quit()
elif g >= 0.9:
  print("A")
elif g >= 0.8:
  print("B")
elif g >= 0.7:
  print("C")
elif g >= 0.6:
  print("D")
elif g < 0.6:
  print("F")
