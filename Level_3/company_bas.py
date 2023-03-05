# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 셔틀버스

from collections import deque


def solution(n: int, t: int, m: int, timeable: list) -> str:
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timeable]
    timetable.sort()
    timetable = deque(timetable)
    current = 540

    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= current:
                candidate = timetable.popleft() - 1
            else:
                candidate = current

        current += t

    h, m = divmod(candidate, 60)

    return str(h).zfill(2) + ':' + str(m).zfill(2)
