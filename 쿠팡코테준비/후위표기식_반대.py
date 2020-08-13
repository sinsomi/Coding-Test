def solve(string):
    stack=[]

    for ch in string:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            num2=int(stack.pop())
            num1=int(stack.pop())
            if ch=='+':
                stack.append(num1+num2)
            elif ch=='*':
                stack.append(num1*num2)
    print(stack[0])
    return 0

solve('34+5*')