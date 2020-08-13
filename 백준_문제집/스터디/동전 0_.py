import sys

n,k = map(int,input().split())
coins=list(int(sys.stdin.readline()) for _ in range(n))

count=0

for i in range(1,n+1):
    coin=coins[-i]
    if k>=coin:
        temp=k//coin
        k-=coin*temp
        count+=temp
print(count)
