# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT> 표 병합

answer = []
graph = [[None for _ in range(51)] for _ in range(51)]
merge_group = []


def update(param: list):
    if len(param) == 3:
        r, c, value = param
        r, c = map(int, [r, c])

        for group in merge_group:
            if (r, c) in group:
                for x, y in group:
                    graph[x][y] = value

        graph[r][c] = value

    if len(param) == 2:
        value1, value2 = param
        for i in range(1, 51):
            for j in range(1, 51):
                if graph[i][j] == value1:
                    graph[i][j] = value2

    return


def merge(param: list):
    r1, c1, r2, c2 = map(int, param)
    if r1 == r2 and c1 == c2:
        return

    new_group = set()
    index = []
    for idx, group in enumerate(merge_group):
        if (r1, c1) in group or (r2, c2) in group:
            index.append(idx)
            new_group = new_group | group

    index.reverse()
    for idx in index:
        merge_group.pop(idx)

    if index:
        value = graph[r1][c1] if graph[r1][c1] is not None else graph[r2][c2]

        if (r1, c1) not in new_group:
            new_group.add((r1, c1))

        if (r2, c2) not in new_group:
            new_group.add((r2, c2))

        for position in new_group:
            x, y = position
            graph[x][y] = value

        merge_group.append(new_group)
    else:
        value = graph[r1][c1] if graph[r1][c1] is not None else graph[r2][c2]

        group = {(r1, c1), (r2, c2)}

        for position in group:
            x, y = position
            graph[x][y] = value

        merge_group.append(group)
    return


def unmerge(param: list):
    r, c = map(int, param)

    index = -1
    for idx, group in enumerate(merge_group):
        if (r, c) in group:
            group = merge_group.pop(idx)
            for position in group:
                x, y = position
                if x == r and y == c:
                    continue
                graph[x][y] = None
            break
    return


def work(command: str):
    do, *param = command.split()

    if do == 'UPDATE':
        update(param)

    if do == 'MERGE':
        merge(param)

    if do == 'UNMERGE':
        unmerge(param)

    if do == 'PRINT':
        r, c = map(int, param)
        answer.append('EMPTY' if graph[r][c] is None else graph[r][c])
    return


def solution(commands: list) -> list:
    for command in commands:
        work(command)

    return answer
