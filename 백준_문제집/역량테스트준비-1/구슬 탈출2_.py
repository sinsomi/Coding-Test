from _collections import deque
import sys

n,m=map(int,input().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
queue=deque()

def init():
    rx, ry, bx, by = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                rx,ry=i,j
            elif board[i][j]=='B':
                bx,by=i,j
    queue.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by]=True

def move(x,y,dx,dy):
    count=0 #이동한 칸 수
    #다음 이동이 벽이거나 현재 위치가 구멍일때까지
    while board[x+dx][y+dy]!='#' and board[x][y] !='O':
        x=x+dx
        y=y+dy
        count+=1
    return x,y,count

def bfs():
    init()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth>10: #10번 이하여야함
            break
        for i in range(4):
            nrx,nry,rc=move(rx,ry,dx[i],dy[i])
            nbx,nby,bc=move(bx,by,dx[i],dy[i])
            if board[nbx][nby]=='O':
                continue
            if board[nrx][nry]=='O':
                print(depth)
                return
            if nrx==nbx and nry==nby:
                if rc>bc:
                    nrx,nry=nrx-dx[i],nry-dy[i]
                else:
                    nbx,nby=nbx-dx[i],nby-dy[i]
            if not visited[nrx][nry][nbx][nby] is True:
                visited[nrx][nry][nbx][nby]=True
                queue.append((nrx,nry,nbx,nby,depth+1))
    print(-1)
bfs()