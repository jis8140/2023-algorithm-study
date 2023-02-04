# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
# n: 문자열 길이
# 시간 복잡도: O(n ^ 2) 공간 복잡도: O(n)

def solution(s: str) -> int:
    if len(s) == 1:
        return 1

    answer = []
    for i in range(1, (len(s) // 2) + 1):
        repeated = s[:i]
        count = 1
        atom = ''

        for j in range(i, len(s), i):
            if repeated != s[j:j + i]:
                st = str(count) + repeated if count != 1 else repeated
                count = 1
                atom += st
                repeated = s[j:j + i]
                continue

            count += 1
        st = str(count) + repeated if count != 1 else repeated
        atom += st

        answer.append(len(atom))

    return min(answer)
