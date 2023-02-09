# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 압축
# n: 문자열의 길이
# 시간 복잡도: O(n ^ 2) 공간 복잡도: O(n ^ 2)

def init() -> list:
    abc = '0abcdefghijklmnopqrstuvwxyz'
    abc = abc.upper()
    return [alphabet for alphabet in abc]
    

def solution(msg: str) -> list:
    dictionary = init()
    
    answer = []
    index, hit, w = 0, 0, ''
    while index < len(msg):
        c = msg[index]
        w += c
        
        if w in dictionary:
            hit = dictionary.index(w)
        else:
            answer.append(hit)
            dictionary.append(w)
            hit = dictionary.index(c)
            w = c
        index += 1
    answer.append(hit)
    
    return answer