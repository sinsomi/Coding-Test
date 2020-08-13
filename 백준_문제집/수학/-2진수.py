import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())
base = 1
ans = []
if n == 0:
	print(0)
else:
	while n :
		#2진법으로 만드는 과정
        # 홀수이면 1을 추가, n에다가 홀수이므로 -base
		if n % 2 :
			ans.append(1)
			n -= base
		# 짝수이면 0을 추가, n에다가 짝수이므로 +base
		else:
			ans.append(0)
		base *= (-1)
		n //= 2

#반대로 출력해주기
for i in reversed(range(len(ans))):
	print(ans[i], end="")