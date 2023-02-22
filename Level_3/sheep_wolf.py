# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 양과 늑대

def solution(info: list, edges: list) -> int:
    answer = []
    visited = [False for _ in range(len(info))]

    def dfs(sheep: int, wolf: int):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True

                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)

                visited[child] = False

    visited[0] = True
    dfs(1, 0)

    return max(answer)
