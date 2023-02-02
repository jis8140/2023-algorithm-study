# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT > 택배 배달과 수거하기
# n: 건물의 수
# 시간 복잡도: O(n) 공간 복잡도: O(1)

def solution(cap: int, n: int, deliveries: list, pickups: list) -> int:
    answer, delivery, pickup = 0, 0, 0

    for index in range(n, 0, -1):
        delivery += deliveries[index - 1]
        pickup += pickups[index - 1]

        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += index * 2

    return answer
