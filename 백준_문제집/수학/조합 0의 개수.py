import sys
n,m=map(int,sys.stdin.readline().split())
count=0
def ft(num):
    return num*ft(num-1) if num > 1 else 1
ans=str(ft(n)//(ft(m)*ft(n-m)))
for i in ans[::-1]:
    if i=='0':
        count+=1
    else:
        break
print(count)