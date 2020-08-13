#<>안에애들은 queue쓰기, 나머지애들은 stack쓰기
import sys

ans=''
flag=0
word=''
for ch in sys.stdin.readline().strip():
    if ch=='<':
        flag^=1
        ans+=word
        word='<'
    elif ch=='>':
        flag ^= 1
        ans += (word+'>')
        word = ''
    elif ch==' ':
        ans+=(word+' ')
        word=''
    else:
        if flag:
            word+=ch
        else:
            word=ch+word
if word:
    ans+=word
print(ans)