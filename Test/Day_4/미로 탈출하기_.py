import sys

n,m=map(int,sys.stdin.readline().split())
miro=[]
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    miro.append(list(sys.stdin.readline().strip()))

dx=[0,1,0,-1] #RDLU
dy=[1,0,-1,0]

def solve(x,y):
    global ans
    if miro[x][y] == 'R':
        nx, ny = x + dx[0], y + dy[0]
    elif miro[x][y]=='D':
        nx, ny = x + dx[1], y + dy[1]
    elif miro[x][y]=='L':
        nx, ny = x + dx[2], y + dy[2]
    elif miro[x][y]=='U':
        nx, ny = x + dx[3], y + dy[3]
    #미로탈출
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        ans+=1
        return ans
    #방문하지 않은 곳이 있다면
    if visited[nx][ny]==0:
        visited[nx][ny]=1
        solve(nx,ny)
    return 0

ans=0
for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        solve(i,j)
print(ans)