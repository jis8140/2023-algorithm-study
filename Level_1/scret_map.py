# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 비밀지도
# n: 지도의 한변의 크기
# 시간 복잡도: O(n) 공간 복잡도: O(n)

def solution(n: int, arr1: list, arr2: list) -> list:
    answer = []

    for i, j in zip(arr1, arr2):
        answer.append(str(bin(i | j)[2:]).rjust(
            n, '0').replace('1', '#').replace('0', ''))

    return answer
