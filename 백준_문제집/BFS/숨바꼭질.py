import sys
from collections import deque

def solve(visited, n, k):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        for nx in (x+1, x-1, 2*x):
            if 0 <= nx < 100001 and visited[nx] == 0: #이범위가 이해안감
                visited[nx] = visited[x] + 1
                queue.append(nx)

n,k = map(int, sys.stdin.readline().split())
visited = [0] * 100001

print(solve(visited,n,k))