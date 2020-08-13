import sys
sys.setrecursionlimit(10000) #sys.setrecursionlimit를 통해 재귀제한범위를늘림
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=0

#연결되어있는 곳을 돌면서 visited[]를 True로 바꿔줌
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(m):
    link=list(map(int,sys.stdin.readline().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

#dfs 돌때마다 cnt증가
for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)
print(cnt)