import sys

n,k=map(int,input().split())
queue=[]
queue.append(n)
visited = [0] * 100001
while queue:
    x=queue.pop(0)
    if x == k:
        break
    for nx in (x-1,x+1,2*x):
        if 0<=nx<100001 and visited[nx]==0:
            visited[nx] = visited[x] + 1
            queue.append(nx)
print(visited[k])