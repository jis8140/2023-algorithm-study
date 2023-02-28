# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 합승 택시 요금

from collections import defaultdict
import heapq

graph = defaultdict(list)


def dijkstra(n: int, start: int):
    pq = [(0, start)]

    visited = [False] * (n + 1)
    weight_dict = defaultdict(int)
    while pq:
        weight, vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True
        weight_dict[vertex] = weight

        for v, w in graph[vertex]:
            if visited[v]:
                continue

            heapq.heappush(pq, (weight + w, v))

    return weight_dict


def solution(n: int, s: int, a: int, b: int, fares: list) -> int:

    # 그래프 생성
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 환승하지 않을 때
    init_weight = dijkstra(n, s)
    answer = init_weight[a] + init_weight[b]

    # 환승을 고려할 때
    for i in range(1, n + 1):
        if init_weight[i] == 0:
            continue

        temp_weight = dijkstra(n, i)
        answer = min(answer, init_weight[i] + temp_weight[a] + temp_weight[b])

    return answer
