# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기
# n: queue 길이
# 시간 복잡도: O(n) 공간 복잡도: O(n)

from collections import deque


def solution(queue1, queue2):
    answer = -1
    queue_1, queue_2 = deque(queue1), deque(queue2)
    index = 0
    total_1, total_2 = sum(queue_1), sum(queue_2)
    max_len = 4 * len(queue_1)

    if (total_1 + total_2) % 2 == 1:
        return -1
    target_number = (total_1 + total_2) / 2

    while index < max_len:
        if total_1 > target_number:
            number = queue_1.popleft()
            queue_2.append(number)
            total_1 -= number
            total_2 += number
        elif total_1 < target_number:
            number = queue_2.popleft()
            queue_1.append(number)
            total_2 -= number
            total_1 += number
        else:
            answer = index
            break
        index += 1
    return answer
