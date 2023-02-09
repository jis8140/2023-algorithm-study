# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 파일명 정렬
# n: 파일명을 포함하는 문자열 배열의 수
# 시간 복잡도: O(nlogn) 공간 복잡도: O(n))

import re


def solution(files: list) -> list:
    name_sorted = []
    for index, file in enumerate(files):
        head = re.split('\d+', file)[0]
        number = re.findall('\d+', file)[0]
        tail = file[len(head) + len(number):]

        name_sorted.append([head.lower(), int(number), tail, index])
    name_sorted.sort(key=lambda x: (x[0], x[1], x[3]))

    return [files[x[3]] for x in name_sorted]
