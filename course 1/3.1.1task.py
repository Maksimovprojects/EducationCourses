hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
	g = r*(h - 40)*1.5 + 40*r
	print(g)
else:
	g = h*r
	print(g)
