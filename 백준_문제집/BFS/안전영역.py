import sys

n=int(input())
matrix=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y,h):
    queue=[]
    queue.append([x,y])
    visit[x][y]=1
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visit[nx][ny]==0 and matrix[nx][ny]>h:
                visit[nx][ny]=1
                queue.append([nx,ny])
    return 0

ans=0
for k in range(max(map(max,matrix))):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0 and matrix[i][j]>k:
                cnt += 1
                bfs(i,j,k)
    ans = max(ans, cnt)

if cnt==0:
    print(1)
else:
    print(ans)