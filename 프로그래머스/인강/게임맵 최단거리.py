from _collections import deque
def solution(maps):
    answer = 0
    visited=[[0]*len(maps[0]) for _ in range(len(maps))]
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    queue=deque()
    queue.append([0,0])
    visited[0][0]=1
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if ny<0 or ny>=len(maps[0]) or nx<0 or nx>=len(maps):
                continue
            if maps[nx][ny]==1 and visited[nx][ny]==0:
                queue.append([ny,nx])
                visited[nx][ny]=visited[x][y]+1
    if visited[len(maps)-1][len(maps[0])-1]==0:
        return -1
    return visited[len(maps)-1][len(maps[0])-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))