import sys
s=input()
t=input()

while True:
    if len(t)<len(s):
        ans=0
        break
    if t==s:
        ans=1
        break
    if t[-1]=='A':
        t=t[:-1]
    elif t[-1]=='B':
        t=t[:-1]
        t=t[::-1]
    else:
        ans=0
        break
print(ans)