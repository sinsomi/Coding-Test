import sys
from copy import deepcopy
import itertools

n,m=map(int,input().split())
matrix=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
empty_wall=[]
virus=[]

for i in range(n):
    for j in range(m):
        #벽을 둘수있는 좌표
        if matrix[i][j]==0:
            empty_wall.append([i,j])
        #바이러스 좌표
        if matrix[i][j]==2:
            virus.append([i,j])

def count_zero(matrix):
    cnt=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                cnt+=1
    return cnt

def bfs(start,candidate,matrix):
    #원본 map을 보존한채 bfs탐색해야함
    matrix=deepcopy(matrix)
    for x,y in candidate:
        matrix[x][y]=1
    queue=[]
    queue.extend(start)
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if matrix[nx][ny]==0:
                queue.append([nx,ny])
                matrix[nx][ny]=2 #바이러스전염
    return count_zero(matrix)

#빈곳에 기둥을 세우기위한 경우의수
candidate=list(itertools.combinations(empty_wall,3))
max_value=0
for i in candidate:
    ans=bfs(virus,i,matrix)
    if max_value<ans:
        max_value=ans
print(max_value)