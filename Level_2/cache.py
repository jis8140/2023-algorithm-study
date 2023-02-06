# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
# n: 도시들의 수
# 시간 복잡도: O(n) 공간 복잡도: O(n)

from collections import deque


def solution(cacheSize: int, cities: list) -> int:
    answer = 0
    city_cache = deque()

    for city in cities:
        city = city.lower()

        if city in city_cache:
            answer += 1
            city_cache.remove(city)
        else:
            answer += 5
        city_cache.append(city)
        if len(city_cache) > cacheSize:
            city_cache.popleft()

    return answer
