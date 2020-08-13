import sys

n,m=map(int,input().split())
game=[[p for p in sys.stdin.readline().strip()] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=False
def dfs(x,y,cnt,color,sx,sy):
    global ans

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        #사이클을 하나 찾으면 종료시키기
        if ans is True:
            return
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        #최소한의 사이클인 4이상이면서 첫번째좌표와 현재좌표가 같으면 True
        if cnt>=4 and sx==nx and sy==ny:
            ans=True
            return True
        if visited[nx][ny]==0 and game[nx][ny]==color:
            visited[nx][ny]=1
            dfs(nx,ny,cnt+1,color,sx,sy)
            visited[nx][ny]=0
    return False


def solve():
    global ans
    for i in range(n):
        for j in range(m):
            sx=i
            sy=j
            visited[sx][sy]=True
            dfs(i,j,1,game[i][j],sx,sy)
            if ans:
                return 'Yes'
    return 'No'
print(solve())