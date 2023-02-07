# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
import math
import re


def is_prime(number: int) -> bool:
    check_num = int(math.sqrt(number)) + 1
    if number < 2:
        return False

    for i in range(2, check_num):
        if number % i == 0:
            return False
    return True


def n_to_k(n: int, k: int) -> str:
    word = ""
    while n:
        word = str(n % k) + word
        n = n // k
    return word


def solution(n: int, k: int) -> int:
    answer = 0
    word = n_to_k(n, k)
    number_list = [x for x in re.split('0+', word) if x != '']

    for number in number_list:
        if is_prime(int(number)):
            answer += 1

    return answer
