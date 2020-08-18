import sys

#3x3
def bythree(x,y,val):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if maps[nx+i][ny+j]==val:
                return False
    return True
#가로
def hori(x,val):
    if val in maps[x]:
        return False
    return True
#세로
def verti(y,val):
    for i in range(9):
        if val==maps[i][y]:
            return False
    return True

def dfs(index):
    # 0을 다채웠을 경우 return
    if index==len(zero):
        for i in range(9):
            print(*maps[i])
        exit()
    # zero에 있는 좌표들에 대해서 dfs탐색
    nx=zero[index][0]
    ny=zero[index][1]
    # 1-10까지 수를 zero 좌표에 넣어봄
    for i in range(1,10):
        if bythree(nx,ny,i) and hori(nx,i) and verti(ny,i):
            maps[nx][ny] = i
            dfs(index + 1)
            maps[nx][ny] = 0

maps=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(9)]
num=list(range(1,10))
zero=[]
for i in range(9):
    for j in range(9):
        if maps[i][j]==0:
            zero.append([i,j])
dfs(0)