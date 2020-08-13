import sys

a,b=sys.stdin.readline().split()
ans=500
for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j]!=b[i+j]:
            count+=1

    if count<ans:
        ans=count

print(ans)