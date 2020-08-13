import sys
from collections import deque

# 변수 선언부
n=int(input())
station=[[] for _ in range(n+1)]
answer=[]
check=[False for i in range(n+1)]
cycle=False

# 역 데이터 입력
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    station[a].append(b)
    station[b].append(a)

# 순환선 찾기
def dfs(cur,start,line): #현재역, 시작역, 경로수
    global cycle

    if cycle is True:
        return

    visited[cur]=True

    for i in range(len(station[cur])):
        next=station[cur][i]
        if visited[next] is False:
            dfs(next,start,line+1)

        elif next==start and line>=2:
            cycle = True
            return

# 지선역에서 가장 가까운 순환선역 찾기 (거리 찾기)
def bfs(a):
    global check
    global visited

    queue=deque()
    queue.append((a,0))
    visited[a]=1

    while queue:
        cur,cnt=queue.pop()

        if check[cur] is True:
            return cnt

        for i in range(len(station[cur])):
            next=station[cur][i]

            if visited[next] is False:
                visited[next]=True
                queue.append((next,cnt+1))

def solve():
    global visited
    global cycle
    global check
    global n

    for i in range(1,n+1):
        cycle=False
        visited = [False for _ in range(n + 1)]
        # DFS를 통해서 현재 역이 순환선이면 cycle = True로 바꾼다.
        dfs(i, i, 0)

        if cycle is True:
            check[i]=True

    for i in range(1, n+1):
        if check[i] is True:
            answer.append(0)
            continue

        visited = [False for _ in range(n + 1)]
        answer.append(bfs(i))

    # 거리를 출력한다.
    for i in range(len(answer)):
        print(answer[i],end=' ')

    return

solve()
