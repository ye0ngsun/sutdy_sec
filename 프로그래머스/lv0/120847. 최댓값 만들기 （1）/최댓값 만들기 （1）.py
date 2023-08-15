def solution(numbers):
    max_n = numbers[0]*numbers[1]
    for x in range(len(numbers)-1):
        for y in numbers[x+1:]:
            z = numbers[x]*y
            if z > max_n:
                max_n = z
    return max_n