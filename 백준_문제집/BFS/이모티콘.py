import sys
from collections import deque

s=int(input())*2   #2차원배열로 생각해줘야하므로!
visited=[[0]*s for _ in range(s)]

queue=deque()
queue.append((1,0))
while queue:
    x,y=queue.popleft()

    if x==s//2:
        print(visited[x][y])
        break
    for nx,ny in ((x,x),(x+y,y),(x-1,y)):
        if nx<0 or nx>=s or ny<0 or ny>=s:
            continue
        #방문안한 곳을 queue에 추가해서 탐색
        if visited[nx][ny]==0:
            queue.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1