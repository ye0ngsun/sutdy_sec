def solution(price):
    answer = price
    if 300000 > price >= 100000:
        answer = price * 95/100
    elif 500000 > price >= 300000:
        answer = price * 90/100
    elif price >= 500000:
        answer = price * 80/100
    return int(answer)