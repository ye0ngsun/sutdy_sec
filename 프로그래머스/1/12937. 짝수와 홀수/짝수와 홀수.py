def solution(num):
    answer = "Odd"
    if num % 2 == 0 or num == 0:
        answer = "Even"
    return answer