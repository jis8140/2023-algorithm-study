# 코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT > 이모티콘 할인행사
# n: user 수 m: emoticons 수
# 시간 복잡도: O(4 ^ m * n) 공간 복잡도: O(4 ^ m)


from itertools import product

rate_list = [10, 20, 30, 40]


def cal_emoticons(rate: list, emoticons: list):
    return [emoticon * ((100 - amount) / 100) for amount, emoticon in zip(rate, emoticons)]


def solution(users: list, emoticons: list) -> list:
    answer = [0, 0]

    for rate in product(rate_list, repeat=len(emoticons)):
        price_list = cal_emoticons(rate, emoticons)
        membership_user, total_price = 0, 0

        for user in users:
            personal_price = 0
            for index, r in enumerate(rate):
                if r >= user[0]:
                    personal_price += price_list[index]

            if personal_price >= user[1]:
                membership_user += 1
            else:
                total_price += personal_price

        if membership_user > answer[0] or (membership_user == answer[0] and total_price >= answer[1]):
            answer[:] = [membership_user, total_price]
    return answer
