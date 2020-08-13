from sys import stdin
input = stdin.readline

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)
def bfs():
    queue=[]
    queue.append([cx,cy])
    while queue:
        x,y=queue.pop(0)
        if x==px and y==py:
            print(visited[x][y])
            return
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                queue.append([nx,ny])


t=int(input())
for _ in range(t):
    n = int(input())
    cx, cy = map(int, input().split())
    px, py = map(int, input().split())
    visited = [[0]*n for _ in range(n)]
    bfs()
