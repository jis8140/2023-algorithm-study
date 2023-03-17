# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 광고 삽입


def str_to_int(time: str) -> int:
    h, m, s = map(int, time.split(':'))

    return h * 3600 + m * 60 + s


def int_to_str(time: int) -> str:
    h, time = divmod(time, 3600)
    m, s = divmod(time, 60)
    h, m, s = map(str, (h, m, s))

    return h.zfill(2) + ':' + m.zfill(2) + ':' + s.zfill(2)


def solution(play_time: str, adv_time: str, logs: list) -> str:
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    dp = [0] * (play_time + 1)
    for log in logs:
        start, end = map(str_to_int, log.split('-'))
        dp[start] += 1
        dp[end] -= 1

    # 구간별 시청자 수 기록
    for index in range(1, play_time + 1):
        dp[index] += dp[index - 1]

    # 모든 구간별 시청자 수 기록
    for index in range(1, play_time + 1):
        dp[index] += dp[index - 1]

    max_view, max_time = 0, 0
    for index in range(adv_time - 1, play_time + 1):
        if index >= adv_time:
            if max_view < dp[index] - dp[index - adv_time]:
                max_view = dp[index] - dp[index - adv_time]
                max_time = index - adv_time + 1

        else:
            if max_view < dp[index]:
                max_view = dp[index]
                max_time = index - adv_time + 1

    return int_to_str(max_time)
