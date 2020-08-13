import sys
from _collections import deque

n,m=map(int,sys.stdin.readline().split())
visited = [[0] * m for _ in range(n)]
miro=[]
for _ in range(n):
    miro.append(list(sys.stdin.readline().strip()))

dx=[0,1,0,-1] #RDLU
dy=[1,0,-1,0]
cnt=0

#탈출구들을 queue에 추가시키는 부분
queue=deque()
for i in range(n):
    for j in range(m):
        if miro[i][j]=='R':
            miro[i][j]=0
        elif miro[i][j]=='D':
            miro[i][j]=1
        elif miro[i][j]=='L':
            miro[i][j] = 2
        elif miro[i][j]=='U':
            miro[i][j] = 3

        x = i + dx[miro[i][j]]
        y = j + dy[miro[i][j]]

        if x<0 or x>=n or y<0 or y>=m:
            visited[i][j]=1
            queue.append((i,j))
            cnt+=1

#역방향으로 탈출하는 부분
while queue:
    #queue에 들어있는 곳들을 시작점으로 해서 역추적을 하여 범위가 넘어가면 cnt를 증가
    x,y=queue.pop()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
    if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]==1:
        continue
    #왜이런식이 들어가는지 이해안감
    if miro[nx][ny]==(i+2)%4:
        visited[nx][ny]=1
        queue.append((nx,ny))
        cnt+=1

print(cnt)