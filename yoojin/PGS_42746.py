def solution(numbers):
    numbers.sort(reverse = True, key = lambda x: str(x) * 3)
    answer = ''
    for i in numbers:
        answer += str(i)
    if answer[0] == '0':
        return '0'
    return answer