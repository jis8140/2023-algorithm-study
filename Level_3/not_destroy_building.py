# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 파괴되지 않은 건물

def solution(board, skill):
    acc_board = [[0 for _ in range(1002)] for _ in range(1002)]

    for command, r1, c1, r2, c2, degree in skill:
        degree = -degree if command == 1 else degree

        acc_board[r1][c1] += degree
        acc_board[r1][c2 + 1] += -degree
        acc_board[r2 + 1][c1] += -degree
        acc_board[r2 + 1][c2 + 1] += degree

    for i in range(1002):
        for j in range(1001):
            acc_board[i][j + 1] += acc_board[i][j]

    for i in range(1001):
        for j in range(1002):
            acc_board[i + 1][j] += acc_board[i][j]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += acc_board[i][j]

            if board[i][j] > 0:
                answer += 1

    return answer
