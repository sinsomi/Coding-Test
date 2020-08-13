from sys import stdin, stdout
from itertools import permutations
input = stdin.readline
print = stdout.write

n, m = map(int, input().split())
for k in permutations(sorted(list(map(int, input().split()))), m):
    print(' '.join(map(str, k))+'\n')