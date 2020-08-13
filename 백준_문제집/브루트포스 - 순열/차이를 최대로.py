from itertools import permutations as per
import sys
n=int(input())
nums=list(map(int,(sys.stdin.readline().split())))
real_ans = 0
for p in per(nums,n):
    ans = 0
    for i in range(n-1):
        ans+=abs(p[i]-p[i+1])
    if real_ans<ans:
        real_ans=ans
    else:
        continue
print(real_ans)