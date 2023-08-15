def solution(slice, n):
    if slice >= n:
        answer = 1
    else:
        answer = n // slice 
        if n % slice != 0:
            answer += 1
    return answer