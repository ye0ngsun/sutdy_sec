def solution(num):
    answer = 0
    cnt = 0
    while num != 1 and cnt < 500:
        if num % 2 == 0:
            num = num / 2
            answer += 1
            cnt += 1
        else:
            num = num * 3 + 1
            answer +=1
            cnt += 1
    if cnt == 500:
        answer = -1
    return answer