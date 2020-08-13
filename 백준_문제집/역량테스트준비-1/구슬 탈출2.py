from _collections import deque
import sys

n,m=map(int,input().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
queue=deque()

def init():
    rx,ry,bx,by=[0]*4 #빨간구슬과 파란구슬의 위치 초기화 0,0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                rx,ry=i,j
            elif board[i][j]=='B':
                bx,by=i,j
    queue.append((rx,ry,bx,by,1)) #위치정보와 depth
    visited[rx][ry][bx][by] = True

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
        rx,ry,bx,by,depth=queue.popleft()
        if depth>10: #10번 이하여야함
            break
        for i in range(4):
            nrx,nry,rc=move(rx,ry,dx[i],dy[i]) #RED
            nbx,nby,bc=move(bx,by,dx[i],dy[i]) #BLUE
            if board[nbx][nby]=='O': #파란구슬이 구멍에 떨어지면 실패
                continue
            if board[nrx][nry]=='O': #빨간구슬이 구멍에 떨어지면 성공
                print(depth)
                return
            #이부분 잘이해안감
            #파란구슬과 빨간구슬이 같은 칸에 있으면 안됨
            if nrx==nbx and nry==nby:
                if rc>bc:         #이동거리가 많은 구슬을 한칸 뒤로
                    nrx,nry=nrx-dx[i],nry-dy[i]
                else:
                    nbx,nby=nbx-dx[i],nby-dy[i]
            #방문여부확인
            if not visited[nrx][nry][nbx][nby] is True:
                visited[nrx][nry][nbx][nby]=True
                queue.append((nrx,nry,nbx,nby,depth+1))
    print(-1)

bfs()