import sys
from _collections import deque
l,w=map(int,input().split())

maps=[[p for p in sys.stdin.readline().strip()] for _ in range(l)]
queue=deque()
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y):
    queue.append([x,y])
    visit=[[0]*w for _ in range(l)]
    visit[x][y]=1
    ans=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=w:
                continue
            if maps[nx][ny]=='L' and visit[nx][ny]==0:
                visit[nx][ny]=visit[x][y]+1
                ans=max(ans,visit[nx][ny])
                queue.append([nx,ny])
    return ans-1 #시작점 1을 빼줌
cnt=0
for i in range(l):
    for j in range(w):
        if maps[i][j]=='L':
            cnt=max(cnt,bfs(i,j))
print(cnt)