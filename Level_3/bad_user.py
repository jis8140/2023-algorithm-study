# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 불량 사용자

from itertools import permutations


def check(user: str, ban: str) -> bool:
    if len(user) != len(ban):
        return False

    for i, j in zip(user, ban):
        if j == '*':
            continue
        if i != j:
            return False

    return True


def solution(user_id: list, banned_id: list) -> int:
    answer = []

    for users in permutations(user_id, len(banned_id)):
        count = 0

        for user, ban in zip(users, banned_id):
            if check(user, ban):
                count += 1

        if count == len(banned_id):
            if set(users) not in answer:
                answer.append(set(users))

    return len(answer)
