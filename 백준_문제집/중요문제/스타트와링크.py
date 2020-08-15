import math
from itertools import combinations as cm

n=int(input())
maps=[list(map(int,input().split())) for _ in range(n)]

min_ans = math.inf

for case in cm(range(1,n+1),n//2): #두팀으로 나눴을 때, case는 첫번째팀경우
    s1=s2=0
    #print(case)
    for i in case:
        for j in case:
            #만약 CASE가 1번,2번,3번이라면 maps[1][1]+maps[1][2]+maps[1][3]+maps[2][1]+...+maps[3][3]
            #print(i,j)
            s1+=maps[i-1][j-1]

    res=set(range(1,n+1))-set(case) #res는 두번째팀 경우
    for i in res:
        for j in res:
            s2+=maps[i-1][j-1]
    min_ans=min(min_ans,abs(s1-s2))
print(min_ans)