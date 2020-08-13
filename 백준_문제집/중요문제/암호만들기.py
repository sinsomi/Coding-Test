from itertools import combinations
import sys
l,c=map(int,input().split())
alpha=sys.stdin.readline().split()
alpha.sort()
mo=['a','e','i','o','u']
mo_cnt=0
ja_cnt=0

#조합구하기(최소 한 개의 모음과 최소 두 개의 자음으로 구성)
for i in combinations(alpha,l):
    for c in i:
        if c in mo:
            mo_cnt+=1
        else:
            ja_cnt+=1
    if mo_cnt>=1 and ja_cnt>=2:
        print(*i)