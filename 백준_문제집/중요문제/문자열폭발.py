string=list(input().strip())
explo=list(input().strip())
stack=[]
cnt=0
for val in string:
    #스택에 넣어줌
    stack.append(val)
    #스택과 폭발문자열 길이가 같으면 값도 같은지 비교
    if len(stack)>=len(explo):
        #뒤에서부터 검사 / 앞에서부터하면 112ab,12ab일때 일치하지 않음
        same=True
        for j in range(-1,(-len(explo))-1,-1):
            if stack[j]!=explo[j]:
                #하나라도 다르면 False, break
                same=False
                break
        #끝까지 다같았다면 폭발시킬수있음
        if same is True:
            a=0
            while a<len(explo):
                stack.pop()
                a+=1
if len(stack)==0:
    print("FRULA")
else:
    for i in stack:
        print(i,end='')