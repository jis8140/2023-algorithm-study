# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# n: record의 수
# 시간 복잡도: O(n) 공간 복잡도: O(n)

def solution(record: list) -> list:
    id_dict = dict()
    log_history = []

    for atom_log in record:
        word = atom_log.split()

        if word[0] == 'Enter':
            id_dict[word[1]] = word[2]

        if word[0] == 'Change':
            id_dict[word[1]] = word[2]
            continue

        log_history.append(word[0] + ' ' + word[1])

    answer = []
    for atom_log in log_history:
        word, user_id = atom_log.split()

        if word == 'Enter':
            answer.append(id_dict[user_id] + '님이 들어왔습니다.')
        else:
            answer.append(id_dict[user_id] + '님이 나갔습니다.')

    return answer
