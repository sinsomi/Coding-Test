import sys

n,m=map(int,input().split())
matrix=[list(map(int,[p for p in sys.stdin.readline().strip()])) for _ in range(n)]
visit=[[0]*m for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
queue=[[0,0]] #시작점
visit[0][0] = 1 #시작점은 방문했으므로 1로 바꾸기

while queue:
    x,y=queue.pop(0)
    #상하좌우
    for i in range(4):
        nx=x+dx[i]  #next x는 x좌표에 dx[i] 더하기
        ny=y+dy[i]  #next y는 y좌표에 dx[i] 더하기
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        #matrix의 다음좌표가 1이고 방문하지 않은경우
        if matrix[nx][ny] and visit[nx][ny]==0:
            queue.append([nx,ny])
            visit[nx][ny]=visit[x][y]+1
print(visit[n-1][m-1])