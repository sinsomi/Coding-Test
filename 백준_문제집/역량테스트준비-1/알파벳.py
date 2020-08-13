import sys

r,c=map(int,sys.stdin.readline().split())
matrix=[list(sys.stdin.readline().strip()) for _ in range(r)]
alpha=[False]*26
ans=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,z):
    global ans
    ans=max(ans,z)
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]

        if nx>=r or nx<0 or ny>=c or ny<0:
            continue

        n=ord(matrix[nx][ny])-ord('A')
        if not alpha[n]:
            alpha[n] = True #방문한 곳은 True로 변경
            dfs(nx,ny,z+1)
            alpha[n]=False  #다른 경로를 탐색할때 다시 초기화시켜줘야하므로
alpha[ord(matrix[0][0])-ord('A')] = True
dfs(0,0,1)
print(ans)