import math
# Assignemnet 4 

teams = ((10, 3), (8, 2), (4, 2), (3, 1))

count = [math.comb(i[0], i[1]) for i in teams]

outcomes = math.prod(count)
 

print(outcomes)
