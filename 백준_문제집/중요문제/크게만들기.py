n,k=map(int,input().split())
num=list(str(input().strip()))
stack=[]
tk=k
for i in range(n):
    #tk(버릴수있는횟수)가 남아있고, stack이 비어있지않고
    #stack마지막 원소가 새로 비교되는 원소보다 작을 경우(while문은 버릴수있는 횟수가 남아있는한
    #stack의 마지막원소가 커질 때까지 버린다.
    while tk>0 and stack and stack[-1]<num[i]:
        stack.pop(-1)
        tk-=1
    stack.append(num[i])
#print(stack)
print(''.join(stack[:n-k]))