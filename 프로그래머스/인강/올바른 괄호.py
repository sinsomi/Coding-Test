def solution(s):
    stack=[]
    #s문자열의 원소들을 검사해봄
    for string in s:
        #stack이 비어있을 때 / 여는괄호가나오면추가, 닫는괄호가나오면 False
        if len(stack)==0:
            if string=='(':
                stack.append(string)
            else:
                return False
        #stack이 비어있지않을때 / 여는괄호가나오면추가, 닫는괄호가 나오면 pop
        elif string=='(':
            stack.append(string)
        elif string==')':
            stack.pop()
    #검사가 끝난후 stack이 비어있는면 짝이 잘맞는것
    if len(stack)==0:
        return True
    return False

print(solution('()()'))