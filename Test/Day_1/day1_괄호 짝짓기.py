def solve():
    n = int(input())
    ori_str = input()
    stack = []
    ans = ''
    for i in range(n):
        #스택이 비었을경우
        if len(stack)==0:
            #닫는 괄호면 False
            if ori_str[i]==')' or ori_str[i]==']' or ori_str[i]=='}' or ori_str[i]=='>':
                return 0
            #여는 괄호면 스택에 추가
            elif ori_str[i]=='(' or ori_str[i]=='[' or ori_str[i]=='{' or ori_str[i]=='<':
                stack.append(ori_str[i])
        #스택이 비지 않았으면서 여는 괄호를 만나면
        elif len(stack)!=0 and (ori_str[i]=='(' or ori_str[i]=='[' or ori_str[i]=='{' or ori_str[i]=='<'):
            #스택에 추가
            stack.append(ori_str[i])
        #스택이 비지 않았으면서 닫는 괄호일경우
        elif len(stack)!=0 and (ori_str[i]==')' or ori_str[i]==']' or ori_str[i]=='}' or ori_str[i]=='>'):
            #쌍이 맞으면 pop()한 뒤에 계속해줌
            if ori_str[i]==')':
                if stack.pop()=='(':
                    continue
                #쌍이 안맞으면 False출력
                else:
                    return 0
            elif ori_str[i]==']':
                if stack.pop()=='[':
                    continue
                else:
                    return 0
            elif ori_str[i]=='}':
                if stack.pop()=='{':
                    continue
                else:
                    return 0
            elif ori_str[i]=='>':
                if stack.pop()=='<':
                    continue
                else:
                    return 0
    if len(stack)==0:
        return 1
    return 0

for i in range(10):
    print('#'+str(i+1)+' '+str(solve()))