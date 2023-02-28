# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 징검다리 건너기

def solution(stones: list, k: int) -> int:
    left, right = 1, 200000000
    while left <= right:
        mid = left + (right - left) // 2

        count = 0
        for stone in stones:
            if mid >= stone:
                count += 1
            else:
                count = 0

            if count >= k:
                break

        if count >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left
