# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# n: board의 크기 m: moves의 크기
# 시간 복잡도: O(nm) 공간 복잡도: O(m)

def solution(board: list, moves: list) -> int:
    answer = 0
    pang = []

    for move in moves:
        for index in range(len(board)):
            if board[index][move - 1]:
                doll = board[index][move - 1]
                board[index][move - 1] = 0

                if pang and doll == pang[-1]:
                    pang.pop(-1)
                    answer += 2
                else:
                    pang.append(doll)

                break

    return answer
