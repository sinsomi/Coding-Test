def solve(n):
    cnt_1 = str(bin(n)).count('1')
    for i in range(n+1,1000001):
        if str(bin(i)).count('1') == cnt_1:
            return i

print(solve(78))