import sys
from collections import deque

m,n,h=map(int,input().split())
tomato=[[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(n)] for _ in range(h)]
visit=[[[0]*m for _ in range(n)] for _ in range(h)]
dx=[1,0,-1,0,0,0]
dy=[0,-1,0,1,0,0]
dz=[0,0,0,0,1,-1]
queue=deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j]==1:
                queue.append([k,i,j])

while queue:
    z,x,y=queue.popleft()
    for i in range(6):
        nz,nx,ny=z+dz[i],x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or nz<0 or nz>=h:
            continue
        if tomato[nz][nx][ny]==0 and visit[nz][nx][ny]==0:
            visit[nz][nx][ny]=visit[z][x][y]+1
            tomato[nz][nx][ny]=1
            queue.append([nz,nx,ny])
#print(visit)
#print(tomato)

ans=max([p for p in max([max(p) for p in visit])])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j]==0 and visit[k][i][j]==0:
                ans=-1
                print(ans)
                exit()

print(ans)