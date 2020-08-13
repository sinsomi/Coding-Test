import sys

n=int(input().strip())
rope=[]
for _ in range(n):
    rope.append(int(sys.stdin.readline().strip()))
rope.sort()
w=0
ans=0
temp=0
for i in range(n):
    w = rope[i] * (n-i)
    if w>=temp:
        temp=w

print(temp)