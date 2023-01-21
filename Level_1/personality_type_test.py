# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
from collections import defaultdict

personality = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
survey_dict = {}
score = [[0, 3], [0, 2], [0, 1], 0, [1, 1], [1, 2], [1, 3]]
score_dict = defaultdict(int)

# 초기화


def init(survey):
    for index, personal in enumerate(survey):
        survey_dict[index] = [personal[0], personal[1]]


# solution
# n: survey 길이 -> 시간 복잡도: O(n) 공간 복잡도: O(1)

def solution(survey, choices):
    answer = ''
    init(survey)

    for index, choice in enumerate(choices):
        if (choice != 4):
            alphabet, number = score[choice - 1]
            score_dict[survey_dict[index][alphabet]] += number

    for personal in personality:
        front, back = personal
        alphabet = front if score_dict[front] >= score_dict[back] else back
        answer += alphabet

    return answer
