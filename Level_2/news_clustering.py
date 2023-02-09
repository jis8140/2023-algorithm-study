# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 뉴스 클러스터링

from collections import Counter


def solution(str1: str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for index in range(len(str1) - 1):
        if str1[index].isalpha() and str1[index + 1].isalpha():
            str1_list.append(str1[index] + str1[index + 1])

    for index in range(len(str2) - 1):
        if str2[index].isalpha() and str2[index + 1].isalpha():
            str2_list.append(str2[index] + str2[index + 1])

    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)

    str_intersection = list((counter1 & counter2).elements())
    str_union = list((counter1 | counter2).elements())

    if len(str_union) == 0 and len(str_intersection) == 0:
        return 65536
    else:
        return int(len(str_intersection) / len(str_union) * 65536)
