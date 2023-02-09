# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 방금그곡

melody_dict = {'A#': 'a', 'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g'}

def changed(akbo: str) -> str:
    for word in melody_dict.keys():
        akbo = akbo.replace(word, melody_dict[word])
    
    return akbo

def cal_time(start: str, end: str) -> int:
    start_hour, start_minute = map(int, start.split(':'))
    end_hour, end_minute = map(int, end.split(':'))
    
    return (end_hour * 60) + end_minute - (start_hour * 60) - start_minute

def solution(m: str, musicinfos: list) -> str:
    melody = changed(m)
    
    answer = []
    for music in musicinfos:
        start, end, name, akbo = music.split(',')
        time = cal_time(start, end)
        akbo = changed(akbo)
        akbo = (akbo * (time // len(akbo)) + akbo[:(time % len(akbo))])
        
        if melody in akbo:
            answer.append((name, time))
    
    answer.sort(key=lambda x: -x[1])
    return '(None)' if not answer else answer[0][0]