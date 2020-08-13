import sys

r,c=map(int,input().split())
matrix=[list(sys.stdin.readline().strip()) for _ in range(r)]
alpha=[False]*26
ans=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y,z):
    global ans
    ans=max(ans,z)
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        n=ord(matrix[nx][ny])-ord('A')
        if not alpha[n]:
            alpha[n]=True
            dfs(nx,ny,z+1)
            alpha[n] = False

alpha[ord(matrix[0][0])-ord('A')]=True
dfs(0,0,1)
print(ans)