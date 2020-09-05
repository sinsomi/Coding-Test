import sys
from collections import deque
sys.setrecursionlimit(100000)
n=int(input().strip())
maps=[list(map(int, [p for p in sys.stdin.readline().split()])) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,h):
    visited[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if maps[nx][ny]>h and visited[nx][ny]==0:
            visited[nx][ny]=1
            dfs(nx,ny,h)

    return

ans=0
for k in range(max(map(max,maps))):
    visited=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if maps[i][j]>k and visited[i][j]==0:
                dfs(i,j,k)
                cnt+=1
    ans=max(ans,cnt)

if cnt==0:
    print(1)
else:
    print(ans)