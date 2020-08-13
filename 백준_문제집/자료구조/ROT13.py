import sys

dict_s='abcdefghijklmnopqrstuvwxyz'
dict_b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sen=sys.stdin.readline()
ans=''
idx=0
for ch in sen:
    if ch==' ':
        ans+=' '
    elif ch.isupper():
        idx=(dict_b.index(ch)+13)%26
        ans+=dict_b[idx]
    elif ch.islower():
        idx=(dict_s.index(ch)+13)%26
        ans+=dict_s[idx]
    elif ch.isdigit():
        ans+=ch
print(ans)