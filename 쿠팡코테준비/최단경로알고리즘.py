import sys
from heapq import heappop,heappush

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heappush(queue,(0, start))

    #힙에 원소가 없을 때 까지 반복.
    while queue:
        cost, pos = heappop(queue)

        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[pos] < cost:
            continue

        for c, next_node in graph[pos]:
            #현재 정점까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_cost = c + cost
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_cost < dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = next_cost
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
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
