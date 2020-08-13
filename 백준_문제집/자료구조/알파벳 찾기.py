import sys
dict='abcdefghijklmnopqrstuvwxyz'
cnt=[-1]*26
word=sys.stdin.readline().strip()
for ch in word:
    idx=dict.index(ch)
    cnt[idx]=word.index(ch)
print(*cnt)