import sys
from _collections import deque

def bfs(x,y):
    cnt=1
    queue.append([x,y])
    maps[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if ny<0 or ny>=n or nx<0 or nx>=n:
                continue
            if maps[nx][ny]==1:
                queue.append([nx,ny])
                maps[nx][ny]=0
                cnt+=1
    return cnt

n=int(input())
maps=[list(map(int,[p for p in sys.stdin.readline().strip()])) for _ in range(n)]
res=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
queue=deque()
for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            res.append(bfs(i,j))
print(len(res))
for i in sorted(res):
    print(i)