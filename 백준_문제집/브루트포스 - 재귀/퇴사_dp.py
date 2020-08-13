import sys
n=int(input())
t,m=[0]*n,[0]*n

for i in range(n):
    t[i],m[i]=map(int,sys.stdin.readline().split())

dp=[0]*25

for i in range(n):
    if dp[i]>dp[i+1]: #현재가 다음날보다 보상이 높다면
        dp[i+1]=dp[i] #다음날 보상은 현재로
    if dp[i+t[i]]<dp[i]+m[i]: #t일후에 받게될 보상이 현재의 보상보다 높다면
        dp[i+t[i]]=dp[i]+m[i] #t일후에 보상을 넣는다
print(dp[n])