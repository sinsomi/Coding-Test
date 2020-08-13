import heapq

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.count = 0

    def push(self, item, priority):
        self.count += 1
        heapq.heappush(self.queue, (priority, item, self.count))

    def pop(self):
        return heapq.heappop(self.queue)

if __name__=="__main__":
    pq=PriorityQueue()
    pq.push('test1',1)
    pq.push('test2',3)
    pq.push('test3',1)
    pq.push('test4',2)
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())

#우선순위 큐
#힙을 사용해서 구현(힙은 각 노드가 하위노드보다 작은(또는큰) 이진트리이다.)
#우선순위가 적은 일부터 처리해주는 자료구조