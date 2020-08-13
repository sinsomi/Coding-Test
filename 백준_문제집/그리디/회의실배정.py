import sys

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting = sorted(meeting, key=lambda x: [x[1], x[0]])

# 빨리 끝나는 것 중 가장 빨리 시작하는 순서대로 더해준다.
max_meeting = 0
start = 0
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        max_meeting += 1

print(max_meeting)