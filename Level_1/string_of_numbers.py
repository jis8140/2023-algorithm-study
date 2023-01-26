# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어
# n: 문자열 길이 / 시간 복잡도: O(n) 공간 복잗도: O(1)


def solution(s: str) -> int:
    number_dict = ['zero', 'one', 'two', 'three',
                   'four', 'five', 'six', 'seven', 'eight', 'nine']

    for number, word in enumerate(number_dict):
        s = s.replace(word, str(number))

    return int(s)
