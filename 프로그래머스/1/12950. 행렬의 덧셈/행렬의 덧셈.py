def solution(arr1, arr2):
    num1 = len(arr1)
    num2 = len(arr1[0])
    answer = []
    a = []
    for i in range(num1):
        for x in range(num2):
            a.append(arr1[i][x] + arr2[i][x])
        answer.append(a)
        a = []
    return answer