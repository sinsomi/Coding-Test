import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

while True:
    w, h = map(int, input().split())
    if not w:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    def dfs(x, y):
        visited[x][y] = True
        global cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            if a[nx][ny] == 1 and visited[nx][ny] is False:
                dfs(nx, ny)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j]==1 and visited[i][j] is False:
                cnt+=1
                dfs(i,j)
    print(cnt)
