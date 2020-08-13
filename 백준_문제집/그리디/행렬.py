import sys

n,m=map(int,sys.stdin.readline().split())
a=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
b=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

#3*3행렬로 1과 0을 바꾸는 함수
def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j]=1-a[i][j]
    return 0

#행렬이 같은지 비교하는 함수
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j]!=b[i][j]:
                return 0
    return 1

#a와 b행렬을 비교하며 행렬의 3*3원소를 뒤집는 부분
#n-2,m-2는 3*3행렬로 바꾸었을때 영향을 미치는 범위
cnt=0
for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j]!=b[i][j]:
            flip(i,j)
            cnt+=1

if check():
    print(cnt)
else:
    print(-1)