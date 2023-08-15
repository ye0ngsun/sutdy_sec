def solution(n, k):
    t = n // 10
    n *= 12000
    k *= 2000
    answer = n+k-t*2000
    return answer