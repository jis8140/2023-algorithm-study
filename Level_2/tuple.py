# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 튜플
import re
from collections import Counter


def solution(s: str) -> list:
    number_list = re.findall('\d+', s)

    return [int(x[0]) for x in Counter(number_list).most_common()]
