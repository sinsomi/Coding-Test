import sys

m,n,k=map(int,input().split())
matrix=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(k)]
visit=[[0]*m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]

for i in matrix:
    for x in range(i[0],i[2]):
        for y in range(i[1],i[3]):
            visit[x][y]=1

def bfs(x,y,cnt):
    queue=[]
    queue.append([x,y])
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visit[nx][ny]==0:
                cnt+=1
                visit[nx][ny]=1
                queue.append([nx,ny])
    return cnt

ans=[]
for i in range(n):
    for j in range(m):
        if visit[i][j]==0:
            cnt = 0
            ans.append(bfs(i,j,cnt))
ans.sort()
print(len(ans))
for i in ans:
    if i==0:
        print(1,end=' ')
    else: print(i,end=' ')