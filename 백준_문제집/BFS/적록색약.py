import sys
n=int(input())
matrix=[list([p for p in sys.stdin.readline().strip()]) for _ in range(n)]
visit=[[0]*n for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y,text):
    queue=[]
    queue.append([x,y])
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if matrix[nx][ny]==text and visit[nx][ny]==0:
                visit[nx][ny]=1
                queue.append([nx,ny])

def bfs2(x,y,text,text2):
    queue=[]
    queue.append([x,y])
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if (matrix[nx][ny]==text or matrix[nx][ny]==text2) and visit[nx][ny]==0:
                visit[nx][ny]=1
                queue.append([nx,ny])


r_cnt,g_cnt,b_cnt,rg_cnt=0,0,0,0
for i in range(n):
    for j in range(n):
        if matrix[i][j]=="R" and visit[i][j]==0:
            bfs(i,j,'R')
            r_cnt+=1
        if matrix[i][j]=="G" and visit[i][j]==0:
            bfs(i,j,'G')
            g_cnt+=1
        if matrix[i][j]=="B" and visit[i][j]==0:
            bfs(i,j,'B')
            b_cnt+=1

visit=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (matrix[i][j]=="R" or matrix[i][j]=="G") and visit[i][j]==0:
            bfs2(i,j,'R','G')
            rg_cnt+=1

print(r_cnt+b_cnt+g_cnt,rg_cnt+b_cnt)