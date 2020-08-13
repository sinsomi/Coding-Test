def solution(dirs):
    x,y=0,0
    cnt=0
    dirs=list(dirs)
    course=[]
    for i in range(len(dirs)):
        if dirs[i]=="U":
            if y<5:
                y += 1
                if [(x,y-1),(x,y)] not in course:
                    course.append([(x,y-1),(x,y)])
                    print(dirs[i], x, y)

        elif dirs[i]=="D":
            if -5<y:
                y-=1
                if [(x,y+1),(x,y)] not in course:
                    course.append([(x,y+1),(x,y)])
                    print(dirs[i],x, y)

        elif dirs[i]=="R":
            if x<5:
                x+=1
                if [(x-1,y),(x,y)] not in course:
                    course.append([(x-1,y),(x,y)])
                    print(dirs[i],x, y)

        elif dirs[i]=="L":
            if x>-5:
                x-=1
                if [(x+1,y),(x,y)] not in course:
                    course.append([(x+1,y),(x,y)])
                    print(dirs[i],x, y)

    return len(course)
print(solution("ULURRDLLU"))