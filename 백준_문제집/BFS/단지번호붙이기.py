import sys

n=int(input())
matrix=[list(map(int,[p for p in sys.stdin.readline().strip()])) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans=[]
def bfs(x,y):
    cnt=1         #cnt+1을 해주는 이유는 현재 있는 위치도 1이므로(i,j)
    queue=[]      #queue 초기화
    queue+=[[x,y]]
    matrix[x][y] = 0  # x,y는 이미방문
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if matrix[nx][ny]:
                cnt+=1
                matrix[nx][ny]=0
                queue+=[[nx,ny]]
    return cnt

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            ans.append(bfs(i,j))

print(len(ans))
for i in sorted(ans):
    print(i)