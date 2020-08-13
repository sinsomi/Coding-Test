import sys

sen=sys.stdin.readline().split()
ans=''
reverse=''
for word in sen:
    for i in range(len(word)):
        if word[i]=='<':
            while(word[i]!='>'):
                ans+=word[i]
                i=i+1
            ans+='>'
print(ans)
