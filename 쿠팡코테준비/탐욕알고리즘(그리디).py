activity = [[1,1,3], [2,2,5], [3,4,7], [4,1,8], [5,5,9], [6,8,10], [7,9,11], [8,11,14], [9,13,16]]

def activitySelection(act):
    result = []

    sortedAct = sorted(act, key=lambda x: x[2])
    print(sortedAct)

    last = 0
    for i in sortedAct:
        if last < i[1]:
            result.append(i)
            last = i[2]

    print("선택된 Activity: ", result)
    result = list(map(lambda x: x[0], result))
    return result

print("선택된 Activity Number: ", activitySelection(activity))