#빈방으로 이동하면 가중치가 0, 벽으로 이동하면 가중치가 1
#일반적인 BFS와 다름!
#최소 경로로 가야하긴한데 그중에서도 벽의개수가가장적게 가야함
#큐를 2개 사용해서, 빈방으로 이동할때는 첫번째큐에넣고
#벽으로이동할때는 두번째큐에넣기
#두개의 큐에 들어간 값을 순서대로 빼면서 처리

import sys
from collections import deque

n,m=map(int,input().split())
miro=[list(map(int,sys.stdin.readline().strip())) for _ in range(m)]
ans=[[0]*n for _ in range(m)] #이부분 [[0]*n]*m 으로하면 2번째예제안됨

dx=[0,-1,0,1]
dy=[1,0,-1,0]

queue=deque()
queue.append((0,0))
miro[0][0]=-1
while queue:
    x,y=queue.pop()

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        #방문한 곳이므로 넘어가기
        if miro[nx][ny]==-1:
            continue
        # 벽이 없을경우
        if miro[nx][ny] == 0:
            ans[nx][ny] = ans[x][y]
            queue.append((nx, ny))
        #벽이 있을경우
        if miro[nx][ny]==1:
            ans[nx][ny]=ans[x][y]+1
            queue.appendleft((nx,ny))
        #nx,ny는 이제 방문한곳이므로 -1로 갱신
        miro[nx][ny]=-1

print(ans[m-1][n-1])