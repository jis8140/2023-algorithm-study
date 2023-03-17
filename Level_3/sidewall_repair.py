# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 외벽 점검


def solution(n: int, weak: list, dist: list) -> int:
    dist.sort(reverse=True)

    repair_list = {()}
    count = 0
    for friend_dist in dist:
        count += 1

        friend_repair = []
        for i, point in enumerate(weak):
            start = point
            ends = weak[i:] + [n + w for w in weak[:i]]
            move = [end % n for end in ends if end - start <= friend_dist]
            friend_repair.append(set(move))

        candidate = set()
        for current in friend_repair:
            for before in repair_list:
                new = current | set(before)
                if len(new) == len(weak):
                    return count

                candidate.add(tuple(new))
        repair_list = candidate

    return -1
