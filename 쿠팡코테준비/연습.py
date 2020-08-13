import sys
from heapq import heappush, heappop

v,e=int(input())
INF=sys.maxsize
dp=[INF]*(v+1)
queue=[]

def Dijkstra(start):
    dp[start]=0 #시작점가중치
    heappush(queue,(0,start))

    while queue:
        cost,pos=heappop(queue)

        if dp[pos]<cost:
            continue

        for c,next_node in graph[pos]:
            next_cost=c+cost
            if next_cost<dp[next_node]:
                dp[next_node]=next_cost
                heappush(queue,(next_cost,next_node))
    return 0

INF = sys.maxsize
V, E = map(int, sys.stdin.readline().split())
#시작점 K
K = int(sys.stdin.readline())
#가중치 테이블 dp
dp = [INF]*(V+1)
queue = []
graph = [[] for _ in range(V + 1)]

#초기화
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    #(가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])