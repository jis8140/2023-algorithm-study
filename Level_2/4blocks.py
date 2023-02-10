# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 프렌즈4블록
# m: 판의 높이 n: 판의 폭
# 시간 복잡도: O(m * m * n) 공간 복잡도: O(m * n)

def solution(m:int, n: int, board: list) -> int:
    board = [list(x) for x in board] 

    matched = True
    while matched:
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j] != '#':
                    matched.append((i, j))

        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = board[i + 1][j] = '#'
        
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], board[i + 1][j]
                    
    return sum(x.count('#') for x in board)
