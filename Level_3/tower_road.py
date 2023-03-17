# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 기둥과 보 설치


def check(answer: set) -> bool:
    for x, y, a in answer:
        # 보
        if a == 1:
            if (x, y - 1, 0) not in answer and (x + 1, y - 1, 0) not in answer and not ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                return False
        # 기둥
        if a == 0:
            if y != 0 and (x, y - 1, 0) not in answer and (x - 1, y, 1) not in answer and (x, y, 1) not in answer:
                return False

    return True


def solution(n: int, build_frame: list) -> list:
    answer = set()

    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            answer.remove((x, y, a))
            if not check(answer):
                answer.add((x, y, a))
        # 설치
        if b == 1:
            answer.add((x, y, a))
            if not check(answer):
                answer.remove((x, y, a))

    answer = list(map(list, answer))
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
