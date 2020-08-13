class Queue:
    def __init__(self):
        self.q = []

    def push(self, data):
        self.q.append(data)

    def pop(self):
        if len(self.q) == 0:
            return False
        return self.q.pop(0)

if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())

#큐란? FIFO(선입선출)
#순서를 보장하기 위한 처리, CPU는 하나의 일이 처리되야 다음 일을 처리