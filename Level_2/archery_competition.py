# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 양궁대회
# n: 화살의 갯수
# 시간 복잡도: O(2 ^ n) 공간 복잡도: O(2 ^ n)


from collections import deque


def bfs(n: int, info: list) -> list:
    answer = []
    total_gap = 0
    queue = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])

    while queue:
        index, score = queue.popleft()

        if sum(score) == n:
            temp_gap = 0
            for i in range(11):
                if info[i] == 0 and score[i] == 0:
                    continue

                temp_gap = (temp_gap - (10 - i)
                            ) if info[i] >= score[i] else (temp_gap + (10 - i))
            if temp_gap <= 0:
                continue

            if total_gap == temp_gap:
                answer.append(score)

            if temp_gap > total_gap:
                total_gap = temp_gap
                answer.clear()
                answer = [score]
            continue

        if sum(score) > n:
            continue

        if index == 10:
            temp = score.copy()
            temp[index] = abs(n - sum(temp))
            queue.append((-1, temp))
            continue

        option_1, option_2 = score.copy(), score.copy()
        option_1[index] = info[index] + 1
        queue.append((index + 1, option_1))
        queue.append((index + 1, option_2))

    return answer


def solution(n: int, info: list) -> list:
    answer = bfs(n, info)

    if not answer:
        return [-1]
    return answer[-1]
