from itertools import permutations
import sys
n=int(input())
nums=[i for i in range(1,n+1)]

for p in permutations(nums,n):
    for i in p:
        print(i,end=' ')
    print()