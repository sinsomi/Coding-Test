import sys

t=int(input())

dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]

def bfs():
    queue=[]
    queue.append([start[0],start[1]])
    visit[start[0]][start[1]]=1
    cnt=0
    while queue:
        x,y=queue.pop(0)
        if x == end[0] and y == end[1]:
            ans = visit[x][y] - 1
            return ans
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if visit[nx][ny]==0:
                visit[nx][ny]=visit[x][y]+1
                queue.append([nx,ny])

for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visit = [[0] * l for _ in range(l)]
    if start[0]==end[0] and start[1]==end[1]:
        print(0)
    else:
        print(bfs())