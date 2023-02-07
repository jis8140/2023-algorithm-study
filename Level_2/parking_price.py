# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# n: 차량의 수
# 시간 복잡도: O(nlogn) 공간 복잡도: O(n)
from collections import defaultdict


def cal_time(time: str) -> int:
    hour, minute = map(int, time.split(':'))
    return (hour * 60) + minute


def cal_price(fees: list, total_time: int) -> int:
    amount, remain = divmod((total_time - fees[0]), fees[2])
    amount = amount + 1 if remain > 0 else amount
    return amount * fees[3]


def init(fees: list, records: list) -> list:
    price_dict = defaultdict(int)
    time_dict = defaultdict(int)
    in_dict = defaultdict(list)
    for record in records:
        time, car_number, way = record.split()
        if way == 'IN':
            in_dict[car_number] = [1, cal_time(time)]
        if way == 'OUT':
            time_dict[car_number] += (cal_time(time) - in_dict[car_number][1])
            in_dict[car_number][0] = 0

    for car_number in in_dict.keys():
        total_time = time_dict[car_number]
        if in_dict[car_number][0] == 1:
            total_time += (cal_time('23:59') - in_dict[car_number][1])

        price_dict[car_number] = fees[1]
        if total_time > fees[0]:
            price_dict[car_number] += cal_price(fees, total_time)

    return price_dict


def solution(fees: list, records: list) -> list:
    price_dict = init(fees, records)
    price_list = [[car_number, price]
                  for car_number, price in price_dict.items()]

    return [x[1] for x in sorted(price_list, key=lambda x: x[0])]
