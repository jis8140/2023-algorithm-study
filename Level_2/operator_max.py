# 코딩테스트 연습 > 2020 카카오 인턴십 > 수식 최대화
# 시간 복잡도: O(1)

from itertools import permutations
import re


def solution(expression: str) -> int:
    operator_rank = list(permutations('*+-', 3))
    number_list = re.split('[*+-]', expression)
    operator_list = [x for x in re.split('[\d]', expression) if x != '']

    print(operator_rank)
    answer = []
    for operator in operator_rank:
        number_copy = number_list.copy()
        operator_copy = operator_list.copy()
        for op in operator:
            while op in operator_copy:
                index = operator_copy.index(op)
                number_copy[index] = str(
                    eval(number_copy[index] + op + number_copy[index + 1]))
                del number_copy[index + 1]
                del operator_copy[index]
                print(number_copy)
                print(operator_copy)
        answer.append(abs(int(number_copy[0])))

    return max(answer)
