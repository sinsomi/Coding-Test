def gcd(x, y):
    while y is not 0:
        x,y=y,x%y
    return x


for _ in range(int(input())):
    n, *a = map(int, input().split())
    s = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            s += gcd(a[i], a[j])
    print(s)