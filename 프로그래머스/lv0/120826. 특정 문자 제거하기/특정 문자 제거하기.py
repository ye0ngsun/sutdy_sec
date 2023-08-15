def solution(my_string, letter):
    A = ''
    for i in my_string:
        if i != letter:
            A += i
    return A