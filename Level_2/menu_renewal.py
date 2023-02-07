# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

from collections import defaultdict
from itertools import combinations


def solution(orders: list, course: list) -> list:
    course_dict = defaultdict(list)
    count_dict = defaultdict(int)

    for order in orders:
        for index in course:
            for comb in combinations(sorted(order), index):
                if comb not in course_dict[index]:
                    course_dict[index].append(comb)
                count_dict[comb] += 1

    answer = []
    for index in course_dict.keys():
        atom_answer = []
        max_count = 2
        for comb in course_dict[index]:
            if max_count == count_dict[comb]:
                atom_answer.append(''.join(comb))

            if max_count < count_dict[comb]:
                max_count = count_dict[comb]
                atom_answer.clear()
                atom_answer = [''.join(comb)]
        answer.extend(atom_answer)

    return sorted(answer)
