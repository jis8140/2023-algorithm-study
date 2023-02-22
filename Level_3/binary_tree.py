# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT > 표현 가능한 이진트리

def dfs(b: str, i: int, depth: int) -> bool:
    if depth == 0:
        return True

    if b[i] == '0':
        if b[i - depth] == '1' or b[i + depth] == '1':
            return False

    l = dfs(b, i - depth, depth // 2)
    r = dfs(b, i + depth, depth // 2)

    return l and r


def two_base(number: int) -> int:
    base = bin(number)[2:]
    x = len(base)

    count = 0
    while x > (pow(2, count) - 1):
        count += 1

    return count


def check(number: int) -> int:
    count = two_base(number)
    number = bin(number)[2:]
    number = number.zfill(pow(2, count) - 1)

    result = dfs(number, len(number) // 2, (len(number) + 1) // 4)

    return 1 if result else 0


def solution(numbers: list) -> list:
    answer = []
    for number in numbers:
        answer.append(check(number))

    return answer
