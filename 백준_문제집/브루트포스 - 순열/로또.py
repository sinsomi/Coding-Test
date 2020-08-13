from itertools import combinations as com
import sys

while(True):
    nums=list(map(int,sys.stdin.readline().split()))
    if nums[0]==0:
        break
    n=nums[0]
    for p in com(nums[1:],6):
        for i in p:
            print(i,end=' ')
        print()
    print()