def solution(array, n):
    answer = 0
    if n in array:
        for i in array: #array는 리스트, i는 원소
            if n == i:
                answer += 1
    return answer