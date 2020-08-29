import heapq
def solution(scoville, K):
    cnt = 0

    #리스트를 힙으로 변환
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        cnt+=1

    return cnt
print(solution([1, 2, 3, 9, 10, 12]	,7))