import random
for x in range(1, 100000000000000000):
  i = random.randint(1,27)
  if i == 1:
    print(" ")
  else:
    print(chr(i+95), end="")
  