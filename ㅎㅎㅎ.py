import sys

def solution():
    stack = []
    vps=list(sys.stdin.readline().strip())
    for i in vps:
        if len(stack)==0:  #스택이 비어있을때
            if i=='(':     #여는괄호는 담기
                stack.append(i)
            else:          #닫는괄호는 틀렸음
                return 'NO'
        elif i=='(':
            stack.append(i)
        elif i==')':
            stack.pop(-1)
    if len(stack)==0:
        return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    print(solution())