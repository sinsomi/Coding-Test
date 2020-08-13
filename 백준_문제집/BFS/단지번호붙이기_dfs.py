import sys

n=int(input())
matrix=[list(map(int,[p for p in sys.stdin.readline().strip()])) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans=[]

def dfs(cnt,x,y):
    matrix[x][y]=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if matrix[nx][ny]:
            cnt+=1
            cnt=dfs(cnt,nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        # dfs는 bfs와 다른점은 cnt를 여기서 1로 초기화 시켜주고 
        # cnt를 매개변수로 넘겨주어야한다
        if matrix[i][j]:
            cnt = 1
            ans.append(dfs(cnt,i,j))
print(len(ans))
for i in sorted(ans):
    print(i)