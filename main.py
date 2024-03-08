import random

flips = int(input("How many flips do you want: "))
coinlist = []
heads = 0
tails = 0
for i in range(flips):
	coinlist.append(random.randint(0,1,))

for i in coinlist:
	if i == 1:
		heads += 1
	else:
		tails += 1

print(f"Heads: {heads}")
print(f"Tails: {tails}")
