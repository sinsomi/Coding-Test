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

#탐색을 이어나감; visited에 1씩 더하면서 저장
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if visited[nx][ny]==0 and tomato[nx][ny]==0:
            queue.append([nx,ny])
            visited[nx][ny]=visited[x][y]+1

#모든 visited에 대해서 각행의 가장큰값
#그 가장큰값들중 가장큰값 -> 바로 가장 마지막에 익은 토마토
ans=max([max(p) for p in visited])

#탐색이 다끝나고 나면, 모든 좌표에대해서 방문하지않으면서 안익은토마토가 있으면
#ans를 -1로 리턴
for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and tomato[i][j]==0:
            ans=-1
print(ans)