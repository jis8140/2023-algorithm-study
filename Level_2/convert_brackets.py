# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 괄호 변환
# n: 문자열의 길이
# 시간 복잡도: O(n ^ 2) 공간 복잡도: O(n)

# 분리 함수
def disunite(brakets: str) -> str:
    left_count, right_count = 0, 0
    for index, braket in enumerate(brakets):
        if braket == '(':
            left_count += 1
        else:
            right_count += 1

        if left_count == right_count:
            return [brakets[:index + 1], brakets[index + 1:]]

    return [brakets[:], '']

# 올바른 괄호 문자열 확인 함수


def is_right(brakets: str) -> bool:
    stack = []

    for braket in brakets:
        if not stack:
            stack.append(braket)
            continue

        if braket == ')' and braket != stack[-1]:
            stack.pop()
        else:
            stack.append(braket)

    return True if not stack else False

# 문자열 괄호 방향을 뒤집어주는 함수


def convert_braket(brakets: str) -> str:
    converted_braket = ''
    for braket in brakets:
        temp = '(' if braket == ')' else ')'
        converted_braket += temp
    return converted_braket

# 올바른 괄호 만들기 함수


def right_brakets(brakets: str) -> str:
    if brakets == '':
        return ''

    if is_right(brakets):
        return brakets

    u, v = disunite(brakets)

    if is_right(u):
        return u + right_brakets(v)
    else:
        return '(' + right_brakets(v) + ')' + convert_braket(u[1:-1])


def solution(p: str) -> str:
    return right_brakets(p)
