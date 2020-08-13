from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(n)]
all_case = [
    #ㅁ모양
    [(0,1), (1,0), (1,1)],
    #ㅣ모양
    [(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    #ㄴ모양
    [(0,1), (0,2), (1,0)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (0,2), (1,2)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (2,0), (2,-1)],
    #Z모양
    [(1,0), (1,1), (2,1)],
    [(0,1), (1,0), (-1,1)],
    [(0,1), (1,0), (1,-1)],
    [(0,1), (1,1), (1,2)],
    #ㅗ모양
    [(0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,-1)],
    [(1,0), (2,0), (1,-1)],
    [(1,0), (1,1), (2,0)]
]

def tetromino(x, y):
    global ans
    #19가지 도형에 대해서 반복
    for i in range(19):
        s = location[x][y]
        #한도형이 좌표를 3개 가지고 있으므로 3번씩 반복
        for j in range(3):
            #nx와 ny를 구해주고
            #s에 location의 nx,ny좌표에 해당하는 값을 더함
            try:
                nx = x+all_case[i][j][0]
                ny = y+all_case[i][j][1]
                s += location[nx][ny]
            except IndexError:
                continue
        ans = max(ans, s)

def solve():
    for i in range (n):
        for j in range(m):
            tetromino(i, j)

ans = 0
solve()
print(ans)