from collections import deque

a,b=map(int,input().split())
queue=deque()
queue.append((a,b,1))

while queue:
    start,end,cnt=queue.pop()

    if start==end:
        print(cnt)
        exit()
        break
    if start*2<=end:
        queue.append((start*2,end,cnt+1))
    if start*10+1<=end:
        queue.append((start*10+1,end,cnt+1))
print(-1)