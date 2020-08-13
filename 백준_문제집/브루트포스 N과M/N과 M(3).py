import sys
import itertools

n,m=map(int,sys.stdin.readline().split())
nums=[i for i in range(1,n+1)]

#중복순열은 product()함수사용
for num in itertools.product(nums,repeat=m):
    for i in num:
        print(i,end=' ')
    print(end='\n')