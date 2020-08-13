import sys
n=int(input())
do=[]
stack=[]
for _ in range(n):
    do.append(sys.stdin.readline().split())
print(do)
for i in range(len(do)):
    if do[i][0]== 'push':
        stack.append(do[i][1])
    elif do[i][0]=='pop':
        if len(stack):
            #가장 위의 정수를 빼라고 했으므로 가장 마지막에 추가된 요소를 빼면된다.
            print(stack.pop(-1))
        else:
            print(-1)
    elif do[i][0] == 'size':
        print(len(stack))
    elif do[i][0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif do[i][0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)