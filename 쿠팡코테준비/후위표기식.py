def solve(string):
    stack=[]
    prior={
        '*':2,
        '+':1,
        '(':0
    }

    for ch in '('+string+')':
        #알파벳일 경우
        if ch.isupper():
            print(ch,end='')

        #여는괄호일 경우
        elif ch=='(':
            stack.append(ch)

        #닫는괄호일 경우
        elif ch==')':
            while True:
                o=stack.pop()
                if o=='(':
                    break
                print(o,end='')

        #연산자일 경우
        else:
            while stack[-1]!='(' and prior[stack[-1]]>=prior[ch]:
                print(stack.pop(),end='')
            stack.append(ch)

    return 0

solve('A*(B+C)')
