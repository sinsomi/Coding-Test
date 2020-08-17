# 백준 2580
import sys

#가로
def horizontal(x,val):
    if val in sdk[x]:
        return False
    return True

#세로
def vertical(y,val):
    for i in range(9):
        if val==sdk[i][y]:
            return False
    return True

#3x3 사각형
def bythree(x,y,val):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if sdk[nx+i][ny+j]==val:
                return False
    return True


def dfs(index):
    #0을 다채웠을 경우 return
    if index==len(zero):
        for i in range(9):
            for j in sdk[i]:
                print(j,end=' ')
            print()
        sys.exit()
    else:
        nx = zero[index][0]
        ny = zero[index][1]
        for i in range(1,10):
            if horizontal(nx,i) and vertical(ny,i) and bythree(nx,ny,i):
                sdk[nx][ny]=i
                dfs(index+1)
                sdk[nx][ny]=0

sdk = [list(map(int, input().split())) for _ in range(9)]
zero = [(x, y) for x in range(9) for y in range(9) if sdk[x][y]==0]
dfs(0)