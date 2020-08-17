import sys

def bfs():
    mx = 0
    #deque를 쓰면 메모리초과남..
    queue = set()
    queue.add((0, 0, matrix[0][0]))

    while queue:
        x, y, sentence = queue.pop()
        mx = max(mx, len(sentence))
        if mx == 26:
            return 26
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if matrix[nx][ny] not in sentence:
                queue.add((nx, ny, sentence + matrix[nx][ny]))
                #print(queue)
    return mx

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
print(bfs())