n=int(input())
ori_str=input()
#숫자를 저장하는 스트링
isnum=''
#연산자를 저장하는 스택
oper_stack=[]
#연산자 우선순위를 저장하는 딕셔너리
pri={
    '+':0,
    '*':1
}

#후위표기식으로 만드는법
#1.숫자를 만나면 ; 스트링에 갖다붙이기
#2.연산자를 만나면 ; 스택에 갖다붙이기
#2-1. 연산자가 우선순위가 높거나 같은게 있을떄까지 다빼기
#2-2. 다빼고나면 그 연산자 추가

#후위표기식으로 만드는 부분
for i in ori_str:
    #숫자이면 스트링에 갖다붙이기
    if i.isdigit():
        isnum+=i
    #연산자이면
    else:
        #연산자스택이 비었으면 그냥 스택에 추가
        if len(oper_stack)==0:
            oper_stack.append(i)
        #연산자 스택에 들어있으면 우선순위 비교해서 높은거 먼저 다빼기
        else:
            while oper_stack and pri[oper_stack[-1]] >= pri[i]:
                isnum += oper_stack.pop()
            oper_stack.append(i)

while(oper_stack):
    isnum+=oper_stack.pop()

#후위표기식 푸는법
#숫자 만나면 push()
#연산자 만나면 int b = pop(), int a = pop()

stack=[]
#후위표기식 푸는 부분
for ch in isnum:
    if ch.isdigit():
        stack.append(ch)
    elif len(stack)>=2:
        b=int(stack.pop())
        a=int(stack.pop())
        if ch=='+':
            stack.append(a+b)
        elif ch=='*':
            stack.append(a*b)
print(stack)