#deque안쓰면 시간초과남!!
import sys
from collections import deque
m,n=list(map(int,sys.stdin.readline().split()))
tomato=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
queue=deque()

#토마토가 1인 부분을 queue에 넣어서 탐색시작점으로!
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i,j])

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if tomato[nx][ny]==0 and visited[nx][ny]==0:
            visited[nx][ny]=visited[x][y]+1
            queue.append([nx,ny])

ans=max([max(p) for p in visited])

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and tomato[i][j]==0:
            ans=-1
print(ans)