import sys
dict='abcdefghijklmnopqrstuvwxyz'
cnt=[0]*26
word=sys.stdin.readline().strip()
for ch in word:
    idx=dict.index(ch)
    cnt[idx]+=1
print(*cnt)