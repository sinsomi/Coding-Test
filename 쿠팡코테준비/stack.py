class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return False
        return self.stack.pop()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())

#스택이란? LIFO(후입선출)
#스택오버플로우 : 무언가를 계속 넣다가 받아들일 수 있는 크기를 초과해서 흘러넘쳐버린것(재귀함수호출에 많이 나오는 에러)
#브라우저에서 뒤로가기, 문서작업에서 컨트롤+Z, 후위표기법, 캐시와 같은 모습으로 많이존재
