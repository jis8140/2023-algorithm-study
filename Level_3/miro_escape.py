# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT > 미로 탈출 명령어

def solution(n, m, x, y, r, c, k):
    def dfs(x, y, r, c):
        answer = ''

        stack = [(x, y, 0, '')]

        while stack:
            x, y, num, path = stack.pop()

            if num == k and (x, y) == (r, c):
                answer = path
                break

            shortest_path = abs(r - x) + abs(c - y)
            if (k - num) < shortest_path or (k - num) % 2 != shortest_path % 2:
                continue

            if x - 1 >= 1:
                stack.append((x - 1, y, num + 1, path + 'u'))

            if y + 1 <= m:
                stack.append((x, y + 1, num + 1, path + 'r'))

            if y - 1 >= 1:
                stack.append((x, y - 1, num + 1, path + 'l'))

            if x + 1 <= n:
                stack.append((x + 1, y, num + 1, path + 'd'))
        return answer

    answer = dfs(x, y, r, c)

    return answer if answer != '' else 'impossible'
