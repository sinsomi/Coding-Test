def solution(bridge_length, weight, truck_weights):
    time=0
    #queue를 다리 길이만큼 만들어주고
    queue=[0]*bridge_length
    s_queue=0

    while queue:
        time+=1
        s_queue-=queue.pop()
        #트럭이 빌때까지 뽑아줌
        if truck_weights:
            # 사용가능한 트럭무게만큼 들어오고 나가고 해서 구현
            if truck_weights[0]+s_queue<=weight:
                s_queue+=truck_weights[0]
                queue.insert(0,truck_weights.pop(0))
                #print(queue)
            else:
                queue.insert(0,0)
                #print(queue)

    return time

print(solution(10,10,[7,4,5,6]))