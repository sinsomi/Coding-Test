#deque안쓰면 시간초과남!!
import sys
from collections import deque
m,n=list(map(int,sys.stdin.readline().split()))
tomato=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

ans=-1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
queue=deque()

#토마토가 1인 부분을 queue에 넣어서 탐색시작점으로!
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i,j])

#탐색을 이어나감; visited에 1씩 더하면서 저장
def bfs():
    global ans
    while queue:
        size=len(queue)
        for _ in range(size):
            x,y=queue.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=n or nx<0 or ny>=m or ny<0:
                    continue
                if visited[nx][ny]==0 and tomato[nx][ny]==0:
                    queue.append([nx,ny])
                    tomato[nx][ny]=1
                    visited[nx][ny]=1
        ans += 1
    return ans

def check():
    global ans
    for i in range(n):
        for j in range(m):
            if tomato[i][j]==0:
                ans=-1
                return
bfs()
check()
print(ans)