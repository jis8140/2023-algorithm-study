# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 다트 게임
# n: 숫자와 연산자 쌍
# 시간 복잡도: O(n) 공간복잡도: O(n)

import re


def init(dart_result: str) -> list:
    number_list = [x for x in re.split('[SDT*#]+', dart_result) if not x == '']
    operator_list = [x for x in re.split('[0-9]+', dart_result) if not x == '']

    return [number_list, operator_list]


def solution(dart_result: str) -> int:
    answer = []
    number_list, operator_list = init(dart_result)

    for number, operator in zip(number_list, operator_list):
        score = int(number)

        if operator[0] == 'D':
            score *= score

        if operator[0] == 'T':
            score *= score * score

        if operator[-1] == '#':
            score = -score

        answer.append(score)

        if operator[-1] == '*':
            answer[-2:] = [x * 2 for x in answer[-2:]]

    return sum(answer)
