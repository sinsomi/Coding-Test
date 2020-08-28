from itertools import combinations

high=[]
for i in range(9):
    high.append(int(input().strip()))

high=sorted(high)

for i in combinations(high,7):
    if sum(list(i))==100:
        for j in i:
            print(j)
        break