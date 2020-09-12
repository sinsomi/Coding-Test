import sys
from collections import deque

n,m=map(int,input().split())
r,c,d=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def changed(d):
    if d==0:   #북->서
        return 3
    elif d==1:  # 동 -> 북
        return 0
    elif d==2:  # 남 -> 동
        return 1
    elif d==3:  # 서 -> 동
        return 2

def find(r,c,d):
    cnt=1
    x=r
    y=c
    arr[x][y] = 2  # 청소한곳 표시
    while True:
        nd=d
        for i in range(4):
            empty = 0
            nd=changed(nd) #현재방향을 기준으로 왼쪽을 탐색(4번반복하면 4방향 다돔)
            nr,nc=r+dx[nd],c+dy[nd]

            if nr<0 or nr>=n or nc<0 or nc>=m:
                continue

            #a
            if arr[nr][nc]==0:
                cnt+=1
                r=nr
                c=nc
                d=nd
                arr[nr][nc]=2
                empty=1
                break

        #c
        if empty==0: #모든칸이 청소되어 있었다면
            #후진
            if d==0:
                r+=1
            elif d==1:
                c-=1
            elif d==2:
                r-=1
            elif d==3:
                c+=1

            #d
            if arr[r][c]==1:
                break
    return cnt
print(find(r,c,d))