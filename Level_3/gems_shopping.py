# 코딩테스트 연습 > 2020 카카오 인턴십 > 보석 쇼핑
# n: gems 리스트의 크기
# 시간 복잡도: O(n) 공간 복잡도: O(n)

from collections import defaultdict


def solution(gems: list) -> list:
    answer = [0, len(gems)]
    length = len(set(gems))

    left, right = 0, 0
    gem_dict = defaultdict(int)
    n = len(gems)
    gem_dict[gems[0]] = 1
    while left < n and right < n:
        if len(gem_dict) == length:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1

                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]

                left += 1
            continue

        right += 1
        if right == n:
            break

        gem_dict[gems[right]] += 1

    return [x + 1 for x in answer]
