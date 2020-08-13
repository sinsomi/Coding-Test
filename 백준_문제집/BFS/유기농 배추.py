import sys

def bfs(i,j):
    queue=[]
    queue.append([i,j])
    visit[i][j]=1
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if matrix[nx][ny] and visit[nx][ny]==0:
                visit[nx][ny]=1
                queue.append([nx,ny])


def solve():
    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and visit[i][j]==0:
                bfs(i, j)
                ans += 1
    print(ans)


t = int(input())
for _ in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    matrix = [[0] * n for _ in range(m)]
    visit= [[0] * n for _ in range(m)]
    for _ in range(k):
        link = list(map(int, input().split()))
        matrix[link[0]][link[1]] = 1
    solve()