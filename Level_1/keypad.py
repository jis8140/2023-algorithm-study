# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
# n: 숫자 리스트 크기 / 시간 복잡도: O(n) 공간 복잡도: O(1)

keypad = {
    0: '13',
    1: '00',
    2: '10',
    3: '20',
    4: '01',
    5: '11',
    6: '21',
    7: '02',
    8: '12',
    9: '22'
}


def solution(numbers: list, hand: str) -> str:
    left_location, right_location = '03', '23'
    answer = ''

    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left_location = keypad[number]

        if number in (3, 6, 9):
            answer += 'R'
            right_location = keypad[number]

        if number in (2, 5, 8, 0):
            ans, left_location, right_location = cal_distance(
                keypad[number], left_location, right_location, hand)
            answer += ans

    return answer


def cal_distance(number_location: str, left: str, right: str, hand: str) -> list:
    left_distance = abs(int(left[0]) - int(number_location[0])) + \
        abs(int(left[1]) - int(number_location[1]))
    right_distance = abs(int(right[0]) - int(number_location[0])) + \
        abs(int(right[1]) - int(number_location[1]))
    answer = ''

    if left_distance > right_distance:
        answer = 'R'
        right = number_location

    if left_distance < right_distance:
        answer = 'L'
        left = number_location

    if left_distance == right_distance:
        answer = 'R' if hand == 'right' else 'L'
        left = number_location if hand == 'left' else left
        right = number_location if hand == 'right' else right

    return [answer, left, right]
