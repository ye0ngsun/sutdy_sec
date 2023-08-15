def solution(sides):
    c = max(sides)
    sides.remove(c)
    if sum(sides)>c:
        return 1
    else:
        return 2