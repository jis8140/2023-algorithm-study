# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT > 개인정보 수집 유효기간

terms_dict = {}

# 초기화


def init(today, terms):
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)

    todays = list(map(int, today.split('.')))

    return todays

# solution


def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = init(today, terms)

    for index, privacy in enumerate(privacies):
        period, term = privacy.split()
        year, month, day = list(map(int, period.split('.')))
        month += terms_dict[term]
        day -= 1

        if (day == 0):
            month -= 1
            day = 28

        if (month / 12 > 1):
            plus, mod = divmod(month, 12)
            if (mod == 0):
                plus -= 1
                mod = 12
            year += plus
            month = mod
        if (today_year > year):
            answer.append(index + 1)
        if (today_year == year and today_month > month):
            answer.append(index + 1)
        if (today_year == year and today_month == month and today_day > day):
            answer.append(index + 1)

    return answer
