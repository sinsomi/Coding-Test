from itertools import combinations
import sys
l,c=map(int,input().split())
input_str=sys.stdin.readline().split()
input_str.sort()
vowels=['a','e','i','o','u']
#조합구하기(최소 한 개의 모음과 최소 두 개의 자음으로 구성)
for c in combinations(input_str,l):
    v_count = 0
    count = 0
    for i in c:
        if i in vowels:
            v_count+=1
        else:
            count+=1
    if v_count>=1 and count>=2:
        print(''.join(c))