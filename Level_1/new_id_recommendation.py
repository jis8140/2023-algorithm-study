# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# n: 문자열 길이 / 시간 복잡도: O(n) 공간 복잡도: O(1)
import re


def solution(new_id: str) -> str:
    answer = step_1(new_id)
    answer = step_2(answer)
    answer = step_3(answer)
    answer = step_4(answer)
    answer = step_5(answer)
    answer = step_6(answer)
    answer = step_7(answer)

    return answer


def step_1(new_id: str) -> str:
    return new_id.lower()


def step_2(new_id: str) -> str:
    return re.sub('[^a-z0-9-_.]', '', new_id)


def step_3(new_id: str) -> str:
    return re.sub('\.+', '.', new_id)


def step_4(new_id: str) -> str:
    return re.sub('^\.|.$', '', new_id)


def step_5(new_id: str) -> str:
    return 'a' if new_id == '' else new_id


def step_6(new_id: str) -> str:
    new_id = new_id[:15] if len(new_id) > 15 else new_id

    return re.sub('\.$', '', new_id)


def step_7(new_id: str) -> str:
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
