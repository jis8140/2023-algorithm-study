# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 등산코스 정하기

from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    answer = [0, 0]
    graph = defaultdict(list)
    intensity = [10000001 for _ in range(n + 1)]
    summit_set = set(summits)

    def dijkstra(gates: list, summits: list):
        pq = []

        for gate in gates:
            heapq.heappush(pq, (0, gate))
            intensity[gate] = 0

        while pq:
            acc_intensity, vertex = heapq.heappop(pq)

            if vertex in summit_set or acc_intensity > intensity[vertex]:
                continue

            for v, w in graph[vertex]:
                max_intensity = max(acc_intensity, w)
                if max_intensity < intensity[v]:
                    intensity[v] = max_intensity
                    heapq.heappush(pq, (max_intensity, v))

        return

    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dijkstra(gates, summits)
    summits.sort()

    answer = [0, 10000001]
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]

    return answer
