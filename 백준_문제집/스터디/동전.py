n,k = map(int,input().split())
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

count = 0
for i in range(n):
    count += k // arr[-1 - i]
    k = k % arr[-1 - i]

print(count)