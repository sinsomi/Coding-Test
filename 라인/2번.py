import sys
from collections import deque

def solution(ball,order):
    result=[]
    stack=[]

    for i in order:
        #i가 젤왼쪽
        if i==ball[0]:
            result.append(ball.pop(0))
            while stack:
                if ball[0] in stack:
                    stack.remove(ball[0])
                    result.append(ball.pop(0))
                else:
                    break
            print('왼')

        # i가 젤오른쪽
        elif i==ball[-1]:
            result.append(ball.pop(-1))
            while stack:
                if ball[-1] in stack:
                    stack.remove(ball[-1])
                    result.append(ball.pop(-1))
                else:
                    break
            print('오')

        #i가 가운데 있을때
        else:
            stack.append(i)
            print('가')

    return result

print(solution([1,2,3,4,5,6],[6,2,5,1,4,3]))
