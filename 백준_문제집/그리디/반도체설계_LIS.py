import sys

n=int(input())
port=list(map(int,sys.stdin.readline().split()))

dp=[0]*n

for i in range(1,n):
    for j in range(i):
        if port[i]>port[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(dp[-1]+1)