def solution(a, b):
    total = 0
    if a-b >= 0:
        while a>=b:
            total += b
            b += 1
    elif a-b < 0:
        while a<=b:
            total += a
            a += 1
    answer = total
    return answer