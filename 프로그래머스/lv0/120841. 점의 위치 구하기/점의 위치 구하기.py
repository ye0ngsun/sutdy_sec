def solution(dot):
    d = dot[0]*dot[1]
    if d > 0:
        answer = 1
        if dot[1]<0:
            answer = 3
    if d < 0:
        answer = 2
        if dot[1]<0:
            answer = 4
    return answer