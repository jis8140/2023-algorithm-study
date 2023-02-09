# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] n진수 게임

remain_dict = ['0', '1', '2', '3', '4', '5', '6',
               '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def n_to_k(n: int, k: int) -> int:
    if n == 0:
        return '0'
    number = ''
    while n:
        number = remain_dict[n % k] + number
        n = n // k
    return number


def solution(n: int, t: int, m: int, p: int):
    answer = ''
    number, index = 0, 1
    while len(answer) < t:
        number_word = n_to_k(number, n)

        for word in number_word:
            if index % m == (p % m) and len(answer) < t:
                answer += word
            index += 1

        number += 1
    return answer
