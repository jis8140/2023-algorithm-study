# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 순위 검색
# n: info의 수 m: query의 수
# 시간 복잡도: O(nlogn + mlogn) 공간 복잡도: O(n + m)

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def init(info: list) -> dict:
    info_dict = defaultdict(list)

    for infomation in info:
        info_list = infomation.split()
        score = int(info_list[-1])
        info_list = info_list[:-1]

        for i in range(5):
            for comb in combinations(info_list, i):
                info_dict[comb].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    return info_dict


def solution(info: list, query: list) -> list:
    answer = []
    info_dict = init(info)

    for question in query:
        query_list = [x for x in question.split() if x != 'and' and x != '-']
        score = int(query_list[-1])
        query_list = query_list[:-1]
        key_query = tuple(query_list)

        number = bisect_left(info_dict[key_query], score)
        answer.append(len(info_dict[key_query]) - number)

    return answer
