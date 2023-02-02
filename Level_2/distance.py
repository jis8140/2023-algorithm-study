# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기
# 시간 복잡도: O(1) 공간 복잡도: O(1)\

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(place: list) -> bool:
    human = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                human.append([0, i, j])
    for person in human:
        queue = deque(person)
        visited = [[0] * 5 for _ in range(5)]

        while queue:
            distance, position_x, position_y = queue.popleft()
            visited[position_x][position_y] = 1

            if distance > 1:
                continue

            for i in range(4):
                nx = position_x + dx[i]
                ny = position_y + dy[i]

                if nx > 4 or nx < 0 or ny > 4 or ny < 0:
                    continue

                if place[nx][ny] == 'X':
                    continue

                if visited[nx][ny] == 1:
                    continue

                if distance < 2 and place[nx][ny] == 'P':
                    return 0

                queue.append([distance + 1, nx, ny])

    return 1


def solution(places: list) -> list:
    return [bfs(place) for place in places]
