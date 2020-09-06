import sys
from collections import deque

def bfs(z,r,c):
    queue = deque()
    queue.append([z,r,c])
    global flag
    flag=False
    while queue:
        z,r,c=queue.popleft()
        for i in range(6):
            nz,nr,nc=z+dz[i],r+dr[i],c+dc[i]
            if nz<0 or nz>=t or nr<0 or nr>=row or nc<0 or nc>=col:
                continue

            if maps[nz][nr][nc]=='E':
                #도달할수 있는지 구별해주는 변수
                flag=True
                visited[nz][nr][nc]=visited[z][r][c]+1
                return visited[nz][nr][nc]

            if maps[nz][nr][nc]=='.' and visited[nz][nr][nc]==0:
                queue.append([nz,nr,nc])
                visited[nz][nr][nc]=visited[z][r][c]+1
    return 0

dz=[-1,1,0,0,0,0]
dr=[0,0,-1,1,0,0]
dc=[0,0,0,0,-1,1]

while True:
    t,row,col=map(int,input().split())

    if t==0 and row==0 and col==0:
        break

    maps=[]
    for _ in range(t):
        maps+=[list([p for p in sys.stdin.readline().strip()] for _ in range(row))]
        input()

    visited=[[[0]*col for _ in range(row)] for _ in range(t)]
    for k in range(t):
        for i in range(row):
            for j in range(col):
                if maps[k][i][j]=='S':
                    cnt=bfs(k,i,j)

    if flag is False:
        print('Trapped!')
    else:
        print('Escaped in',cnt,'minute(s).')
