from itertools import permutations
import sys
n=int(input())
nums=[p for p in range(1,10001)]
current=tuple(map(int,nums))
re_nums=tuple(map(int,sorted(nums,reverse=True)))
count=0

nums=[p for p in range(1,10001)]

for p in permutations(nums,n):
    if p==re_nums:
        print(-1)
        break
    if count==1:
        for i in p:
            print(i,end=' ')
        break
    if p==current:
        count += 1
        continue