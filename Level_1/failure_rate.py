# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율
# n: N의 크기 m: 플레이어 수
# 시간 복잡도: O(nm) 공간 복잡도: O(n + m)


def solution(N: int, stages: list) -> list:
    failure_list = []
    clear = 0

    for index in range(N, -1, -1):
        failure = stages.count(index + 1)
        clear += failure
        if clear:
            failure_list.append(failure / clear)
        else:
            failure_list.append(0)

    failure_list.reverse()

    dict = {i + 1: failure_list[i] for i in range(N)}
    answer = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    answer = [i for i, j in answer]

    return answer
