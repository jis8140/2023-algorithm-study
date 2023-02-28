# 코딩테스트 연습 > 2020 카카오 인턴십 > 경주로 건설

import heapq
from sys import maxsize


def solution(board: list) -> int:
    n = len(board)
    costBoard = [[[maxsize] * n for _ in range(n)] for _ in range(4)]

    for i in range(4):
        costBoard[i][0][0] = 0

    pq = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while pq:
        cost, x, y, d = heapq.heappop(pq)

        for dx, dy, dd in ((1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)):
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny]:
                continue

            price = cost + (100 if d == dd else 600)

            if costBoard[dd][nx][ny] > price:
                costBoard[dd][nx][ny] = price
                heapq.heappush(pq, (price, nx, ny, dd))

    return min([costBoard[i][-1][-1] for i in range(4)])
