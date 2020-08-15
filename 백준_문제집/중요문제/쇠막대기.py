import sys
vps=sys.stdin.readline().strip()
vps=vps.replace('()','*')
stack=[]
ans=0

for val in vps:
    if val=='(':
        stack.append(val)
        ans+=1
    elif val==')':
        stack.pop(-1)
    else:   #레이저
        ans+=len(stack)
print(ans)