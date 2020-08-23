def solution(bakery_schedule, current_time, K):
    time_table = []
    num_table = []
    index = 0

    ## time schedule and number split two list
    for schedule in bakery_schedule:
        time, num = schedule.split(' ')
        hour, minute = time.split(':')
        time = 60*int(hour) + int(minute)
        num = int(num)
        time_table.append(time)
        num_table.append(num)

    ## current time
    hour, minute = current_time.split(':')
    current_time = 60*int(hour) + int(minute)

    ## index is current time located at time_schedule
    for i, time in enumerate(time_table):
        index = i
        if time == current_time or current_time < time:
            break
    ## if amount number is smaller than target number K
    if K > sum(num_table[index:]):
        return -1

    ## final check
    for time, num in zip(time_table[index:], num_table[index:]):
        K -= num
        if K <= 0: return time - current_time

    return -1