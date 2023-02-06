# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 후보키

from itertools import combinations


def solution(relation: list) -> int:
    row = len(relation)
    column = len(relation[0])

    answer = []
    for i in range(1, column + 1):
        field_key = combinations(range(column), i)

        for combi in field_key:
            record_tuple = [tuple([item[field] for field in combi])
                            for item in relation]

            if len(set(record_tuple)) != row:
                continue

            minimum = True
            for candidate_key in answer:
                if candidate_key.issubset(set(combi)):
                    minimum = False
                    break

            if minimum:
                answer.append(set(combi))

    return len(answer)
