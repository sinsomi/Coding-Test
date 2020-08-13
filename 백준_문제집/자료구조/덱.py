import sys
n=int(input())
do=[]
deque=[]
for _ in range(n):
    do.append(sys.stdin.readline().split())
for i in range(len(do)):
    if do[i][0]== 'push_front':
        deque.insert(0,do[i][1])
    elif do[i][0]=='push_back':
        deque.append(do[i][1])
    elif do[i][0]=='pop_front':
        if len(deque):
            print(deque.pop(0))
        else:print(-1)
    elif do[i][0]=='pop_back':
        if len(deque):
            print(deque.pop())
        else:print(-1)
    elif do[i][0]=='size':
        print(len(deque))
    elif do[i][0]=='empty':
        if len(deque):
            print(0)
        else:print(1)
    elif do[i][0]=='front':
        if len(deque):
            print(deque[0])
        else: print(-1)
    elif do[i][0]=='back':
        if len(deque):
            print(deque[-1])
        else:print(-1)