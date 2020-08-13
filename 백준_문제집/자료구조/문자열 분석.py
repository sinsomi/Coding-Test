from sys import stdin

for i in stdin:
    cnt=[0]*4
    for ch in (i):
        if ch.islower():
            cnt[0] += 1
        elif ch.isupper():
            cnt[1] += 1
        elif ch.isdigit():
            cnt[2] += 1
        else:
            cnt[3] += 1
    cnt[3]-=1
    print(*cnt)
