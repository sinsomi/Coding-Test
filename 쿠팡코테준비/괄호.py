def solve(string):
    stack=[]
    for ch in string:
        #스택이 비었는데, 닫는 괄호인 경우
        if len(stack)==0 and (ch==')' or ch==']' or ch=='}'):
            return False

        #여는 괄호인 경우
        if ch=='(' or ch=='[' or ch=='{':
            stack.append(ch)

        #스택이 비지 않았으면서, 닫는 괄호인 경우
        elif len(stack)!=0:
            if ch==')':
                if stack.pop()=='(':
                    continue
                else:
                    return False
            if ch == ']':
                if stack.pop() == '[':
                    continue
                else:
                    return False
            if ch=='}':
                if stack.pop()=='{':
                    continue
                else:
                    return False

    #for문을 다 한뒤에 stack이 비었으면 True
    return True if len(stack)==0 else False

print(solve('([{])'))