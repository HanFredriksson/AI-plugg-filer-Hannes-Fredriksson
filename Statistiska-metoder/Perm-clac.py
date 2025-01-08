import math

teams = ((10, 3), (8, 2), (4, 2), (3, 1))
count = []

for i in teams:
    nr = math.comb(i[0], i[1])
    count.append(nr)

print(count)
