def solution(n):
    answer = n // 7
    if n % 7 == 0:
        return answer
    else:
        return answer+1