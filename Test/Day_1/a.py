ori_str=input()
isnum=''
oper_stack=[]
pri={
    '+':0,
    '*':1
}
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

