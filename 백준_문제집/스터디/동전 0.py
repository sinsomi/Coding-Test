import sys

n,k = map(int,input().split())
coins=list(int(sys.stdin.readline()) for _ in range(n))

total=0
count=0

while k!=total:
    for i in reversed(coins):
        if i<=k:
            total+=i
            count+=1
            print(total)
            break

print(count)
