import sys

def solve(string):
    stack=[]
    #문자열string에 들어있는 문자에 대해
    for ch in string:
        #만약 stack이 비어있는데 ')'나오면 쌍이 안맞는것이므로 NO
        if len(stack) == 0 and ch == ')':
            return 'NO'
        #만약 '('라면 stack에 추가
        if ch == '(':
            stack.append(ch)
        #만약 ')'라면(stack이 비어있지 않으면서 ')'일경우)
        else:
            #만약 맨마지막 요소가 '('이거이면
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
    if len(stack)==0:
        return 'YES'
    return 'NO'

t=int(input())
ans=[]
for _ in range(t):
    strs=sys.stdin.readline().strip()
    ans.append(solve(strs))
for i in ans:
    print(i)

