import sys

n,m=list(map(int,sys.stdin.readline().split()))
matrix=[list(map(int,[pos for pos in sys.stdin.readline().strip()])) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
queue=[[0,0]]   #queue에 시작점 넣어두기
visit[0][0] = 1  #시작점은 1로 바꾸기


while queue:
    x,y=queue.pop(0)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if matrix[nx][ny] and visit[nx][ny]==0:
            visit[nx][ny]=visit[x][y]+1
            queue.append([nx, ny])
visit[x][y]