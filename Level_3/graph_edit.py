# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 표 편집

def solution(n: int, k: int, cmd: list):
    answer = ['O' for _ in range(n)]
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    current = k
    stack = []

    for command in cmd:
        param = command.split()

        if param[0] == 'U':
            for _ in range(int(param[1])):
                current = table[current][0]

        if param[0] == 'D':
            for _ in range(int(param[1])):
                current = table[current][1]

        if param[0] == 'C':
            answer[current] = 'X'
            prev, next = table[current]
            stack.append([prev, current, next])
            if next == None:
                current = table[current][0]
            else:
                current = table[current][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        if param[0] == 'Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

    return ''.join(answer)
