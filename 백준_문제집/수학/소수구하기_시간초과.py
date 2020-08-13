import sys

ans=[]
m,n=map(int,sys.stdin.readline().split())
for i in range(m,n+1,1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        ans.append(i)
for a in ans:
    print(a)