from itertools import combinations

n,m = map(int, input().split())

#1부터 n까지 숫자들을 m개씩 조합한 것
p=combinations(range(1,n+1),m)

for i in p:
    print(' '.join(map(str,i)))